from dataclasses import dataclass


@dataclass
class ClickHouseConfig:
    host: str
    database: str
    user: str
    password: str
    port: int
    retries: int
    delay: int
