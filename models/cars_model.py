from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Boolean, Float
from config.db import meta
import datetime

cars_model = Table(
    'cars', meta,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True, ),
    Column('event_id', Integer, nullable=False),
    Column('originalDaysOnSale', Integer),
    Column('is_vin', Boolean, nullable=False),
    Column('vin', String(50)),
    Column('status', String(50), nullable=False),
    Column('public_url', String(100), nullable=False),
    Column('brand', String(100), nullable=False),
    Column('model', String(100), nullable=False),
    Column('generation', String(100)),
    Column('year', Integer, nullable=False),
    Column('engine_capacity', Float),
    Column('engine_type', String(50), nullable=False),
    Column('transmission_type', String(50), ),
    Column('body_type', String(70),),
    Column('drive_type', String(70),),
    Column('mileage_km', Integer, ),
    Column('color', String(70),),
    Column('interior_color', String(50), ),
    Column('interior_material', String(70), ),
    Column('car_description', Text),
    Column('location_short', String(70), nullable=False),
    Column('location_full', String(70), nullable=False),
    Column('price_usd', Float),
    Column('price_byn', Float),
    Column('price_rub', Float),
    Column('price_eur', Float),
    Column('seller_phone', String(20)),
    Column('seller_phone2',  String(20)),
    Column('seller_name', String(100)),
    Column('exchange', String(100)),
    Column('published_at', DateTime, ),
    Column('refreshed_at', DateTime, ),
    Column('renewed_at', DateTime, ),
    Column('delete_at', DateTime),
)
