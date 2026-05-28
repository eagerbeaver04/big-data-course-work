import random
import time
from sqlalchemy import Table, Column, Integer, Float, MetaData

from utils.click_house_session import ClickHouseSession, ClickHouseConfig
from utils.load_db_env import load_db_env

metadata = MetaData()
events = Table(
    "events",
    metadata,
    Column("id", Integer),
    Column("x1", Float),
    Column("x2", Float),
    Column("x3", Float),
    Column("label", Float),
)


def main():
    config: ClickHouseConfig = load_db_env()
    with ClickHouseSession(config) as session:
        while True:
            feature1 = random.uniform(0, 100)
            feature2 = random.uniform(0, 50)
            feature3 = random.uniform(0, 30)
            label = 1.0 if (feature1 + feature2 > 75) else 0.0

            # Генерируем id заранее
            row_id = random.randint(1, 1000)

            ins = events.insert().values(
                id=row_id,
                x1=feature1,
                x2=feature2,
                x3=feature3,
                label=label,
            )
            session.execute(ins)
            session.commit()
            print(
                f"Inserted id={row_id}, x1={feature1:.2f}, x2={feature2:.2f}, x3={feature3:.2f}, label={label}"
            )
            time.sleep(1)


if __name__ == "__main__":
    main()
