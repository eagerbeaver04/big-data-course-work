from dotenv import load_dotenv
import os

from utils.structures import ClickHouseConfig

load_dotenv()


def load_db_env() -> ClickHouseConfig:
    return ClickHouseConfig(
        os.getenv("CLICKHOUSE_HOST"),
        os.getenv("CLICKHOUSE_DATABASE"),
        os.getenv("CLICKHOUSE_USER"),
        os.getenv("CLICKHOUSE_PASSWORD"),
        int(os.getenv("DATABASE_DATA_PORT", 9000)),
        int(os.getenv("CLICKHOUSE_RETRIES", 5)),
        int(os.getenv("CLICKHOUSE_DELAY", 5)),
    )
