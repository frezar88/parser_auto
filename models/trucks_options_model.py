from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Boolean, Float, JSON
from config.db import meta
import datetime

trucks_options_model = Table(
    'trucks_options', meta,
    Column('id', Integer, primary_key=True, autoincrement=True, index=True, ),
    Column('truck_id', ForeignKey('trucks.id', ondelete='CASCADE'), nullable=False),
    Column('photo', JSON),
    Column('abs', Boolean),
    Column('heater', Boolean),
    Column('conditioner', Boolean),
    Column('cruise_control', Boolean),
    Column('navigation', Boolean),
    Column('mirror_heating', Boolean),
    Column('safety_bags', Boolean),
    Column('berth', Boolean),
    Column('tachograph', Boolean),
    Column('central_locking', Boolean),
    Column('three_way_unloading', Boolean),
    Column('cruise_control', Boolean),
    Column('side_unloading', Boolean),
    Column('rear_unloading', Boolean),
)
