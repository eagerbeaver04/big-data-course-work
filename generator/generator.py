import random
import time

from utils.click_house_session import ClickHouseSession, ClickHouseConfig
from utils.load_db_env import load_db_env
from utils.tables import get_event_table


def main():
    config: ClickHouseConfig = load_db_env()
    with ClickHouseSession(config) as session:
        events = get_event_table()
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
