import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from utils.structures import ClickHouseConfig


class ClickHouseSession:
    def __init__(self, config: ClickHouseConfig):
        self.url = f"clickhouse://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
        self.retries = config.retries
        self.delay = config.delay
        self.engine = None
        self.session = None

    def __enter__(self):
        attempt = 0
        last_exception = None
        while attempt < self.retries:
            try:
                self.engine = create_engine(self.url)
                with self.engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                Session = sessionmaker(bind=self.engine)
                self.session = Session()
                print("Connected to ClickHouse")
                return self.session
            except Exception as e:
                last_exception = e
                attempt += 1
                print(f"Waiting ClickHouse (attempt {attempt}/{self.retries}): {e}")
                time.sleep(self.delay)
        raise ConnectionError(
            f"Could not connect after {self.retries} attempts for {self.url}"
        ) from last_exception

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
        if self.engine:
            self.engine.dispose()
