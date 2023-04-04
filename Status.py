import datetime
from time import sleep

from utils.DataBase import DataBase
from models.cars_model import cars_model
from models.trucks_model import trucks_model
from models.status_change import status_change_model
from utils.Requester import Requester
from utils.Vin import Vin
import os
import requests


class Status(DataBase, Requester):
    def __init__(self):
        super().__init__()
        self.cars = self.get_active_or_archived_cars()
        self.trucks = self.get_active_or_archived_trucks()

    def get_active_or_archived_cars(self):
        cars = self.data_base.execute(cars_model.select().where(cars_model.c.status != 'delete')).fetchall()
        return cars

    def get_active_or_archived_trucks(self):
        trucks = self.data_base.execute(
            trucks_model.select().where(trucks_model.c.status != 'delete')).fetchall()
        return trucks

    def check_actual_status_car(self):
        vin_parser = Vin()
        for index, car in enumerate(self.cars):
            sleep(0.6)
            print(f"cars- {index} из {len(self.cars)}")
            status = self.request_check_car_status(car_id=car.event_id)
            if not car.status == status:
                self.data_base.execute(cars_model.update().values(
                    status=status
                ).where(cars_model.c.event_id == car.event_id))
                self.data_base.execute(status_change_model.insert().values(
                    event_id=car.event_id,
                    status=status,
                    date=datetime.datetime.now(),
                    type_car='car'
                ))
            if car.is_vin and not car.vin:
                vin_parser.get_vin(car_type='car', car_id=car.id, event_id=car.event_id)

    def check_actual_status_truck(self):
        vin_parser = Vin()
        for index, car in enumerate(self.trucks):
            sleep(0.6)
            print(f"truck- {index} из {len(self.trucks)}")
            status = self.request_check_car_status(car_id=car.event_id)
            if not car.status == status:
                self.data_base.execute(trucks_model.update().values(
                    status=status
                ).where(trucks_model.c.event_id == car.event_id))
                if status == 'delete':
                    self.data_base.execute(trucks_model.update().values(
                        delete_at=datetime.datetime.now()
                    ).where(trucks_model.c.event_id == car.event_id))
                self.data_base.execute(status_change_model.insert().values(
                    event_id=car.event_id,
                    status=status,
                    date=datetime.datetime.now(),
                    type_car='truck'
                ))
            if car.is_vin and not car.vin:
                vin_parser.get_vin(car_type='truck', car_id=car.id, event_id=car.event_id)

    def check_all_status(self):
        try:
            self.check_actual_status_car()
            self.check_actual_status_truck()
        except Exception as e:
            self.error_logging(msg=e, method='check_all_status(70)', logs_path='../logs/log.txt')


Status().check_all_status()
