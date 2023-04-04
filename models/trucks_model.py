from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Boolean, Float
from config.db import meta
import datetime

trucks_model = Table(
    'trucks', meta,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True, ),
    Column('event_id', Integer, nullable=False),
    Column('originalDaysOnSale', Integer),
    Column('is_vin', Boolean, nullable=False),
    Column('vin', String(50)),
    Column('status', String(50), nullable=False),
    Column('public_url', String(100), nullable=False),
    Column('brand', String(100), nullable=False),
    Column('model', String(100), nullable=False),
    Column('year', Integer, nullable=False),
    Column('engine_capacity', Float),
    Column('engine_type', String(50), ),
    Column('transmission_type', String(50), ),
    Column('modification', String(100), ),
    Column('wheelFormula', String(100), ),
    Column('minifiedType', String(100), ),
    Column('body_type', String(100)),
    Column('mileage_km', Integer),
    Column('location_short', String(70), nullable=False),
    Column('location_full', String(70), nullable=False),
    Column('price_usd', Float, nullable=False),
    Column('price_byn', Float, nullable=False),
    Column('price_rub', Float, nullable=False),
    Column('price_eur', Float, nullable=False),
    Column('seller_phone',  String(20)),
    Column('seller_phone2',  String(20)),
    Column('seller_name', String(100)),
    Column('exchange', String(100)),
    Column('car_description', Text),
    Column('published_at', DateTime, nullable=False),
    Column('refreshed_at', DateTime, ),
    Column('renewed_at', DateTime, ),
    Column('delete_at', DateTime),

)
