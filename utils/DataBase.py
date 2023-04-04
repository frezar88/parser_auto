from config.db import con
from models.cars_model import cars_model
from models.trucks_model import trucks_model


class DataBase:
    def __init__(self):
        self.data_base = con

    def save_vin_number_to_data_base(self, car_id, car_type, vin):
        if car_type == 'car':
            self.data_base.execute(cars_model.update().values(
                vin=vin
            ).where(cars_model.c.id == car_id))
        if car_type == 'truck':
            self.data_base.execute(trucks_model.update().values(
                vin=vin
            ).where(trucks_model.c.id == car_id))
