from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Boolean, Float
from config.db import meta
import datetime

status_change_model = Table(
    'status_change', meta,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True, ),
    Column('event_id', Integer, nullable=False),
    Column('status', String(50), nullable=False),
    Column('date', DateTime, nullable=False),
    Column('type_car', String(50), nullable=False),
)
