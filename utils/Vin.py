from utils.DataBase import DataBase
from utils.Requester import Requester
from utils.ErrorHandler import ErrorHandler


class Vin(DataBase, Requester):
    def __init__(self):
        super().__init__()
        self.api_keys = ['x0e24798cf9429dc0891e28', 'md95d5da92b50d47ea0c495', 'ccea327a1a412c058208ee7',
                         'x6f3763e079c37714c9bef1', 'jc579ef830f1ddb1392397d', 'j900d5546da20b67d01d9a2',
                         'ce26208f8c4fafdb7401eb2', 'h058d51d0202c5fadfab743', 's748ab69083226079d953aa',
                         'l4f1435725534e908e8dd68', 've1d7a5178adee247589c17', 'z8761eb8d91c8aa3fa09e0e',
                         'y2bf697daa722f1aa416fba', 'cbe09c1d47f244995aa5d93', 'gce4bfa2497c3d4d29aae27',
                         'c54ce0859faafadd1fe8e93', 'h4f86ed71f71797914aef20', 'e4688fb8a4bd1261ec2fde2',
                         'f5e958fb30ee4e625d44b42', 'of3aab0105b90f88904f67d', 'sd4eeb9f3dd5d7390012ce4']
        self.current_api_counter = 0
        self.counter = 0

    def increment_counter(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

    def set_zero_counter(self):
        self.counter = 0

    def set_zero_current_api_counter(self):
        self.current_api_counter = 0

    def increment_current_api_counter(self):
        self.current_api_counter += 1

    def get_current_api_counter(self):
        return self.current_api_counter

    def generate_auth_headers(self, api_key):
        headers = self.generate_headers()
        headers['x-api-key'] = api_key
        return headers

    def get_vin(self, car_type, car_id, event_id):
        try:
            if car_type == 'car':
                if self.counter > len(self.api_keys) - 1:
                    print('закончили с винами')
                    return
                vin = self.request_get_vin_car(event_id=event_id, headers=self.generate_auth_headers(
                    self.api_keys[self.counter]))
                if vin:
                    self.save_vin_number_to_data_base(car_id=car_id, car_type='car', vin=vin)
                self.increment_current_api_counter()
                if self.get_current_api_counter() == 30:
                    self.set_zero_current_api_counter()
                    self.increment_counter()
            if car_type == 'truck':
                if self.counter > len(self.api_keys) - 1:
                    print('закончили с винами')
                    return
                vin = self.request_get_vin_truck(event_id=event_id, headers=self.generate_auth_headers(
                    self.api_keys[self.counter]))
                if vin:
                    self.save_vin_number_to_data_base(car_id=car_id, car_type='truck', vin=vin)
                self.increment_current_api_counter()
                if self.get_current_api_counter() == 30:
                    self.set_zero_current_api_counter()
                    self.increment_counter()
        except Exception as e:
            self.error_logging(msg=e, method='get_vin(67)', logs_path='../logs/log.txt')
