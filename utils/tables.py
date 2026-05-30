from sqlalchemy import Table, Column, Integer, Float, MetaData

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


def get_event_table() -> Table:
    return events
