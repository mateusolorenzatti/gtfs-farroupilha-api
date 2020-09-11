
import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table, create_engine)
from sqlalchemy.sql import func

from core.config import settings

from databases import Database

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
)

metadata = MetaData()

# notes = Table(
#     "notes",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String(50)),
#     Column("description", String(50)),
#     Column("created_date", DateTime, default=func.now(), nullable=False),
# )

database = Database(settings.SQLALCHEMY_DATABASE_URI)