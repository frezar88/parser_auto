from time import sleep

from dotenv import load_dotenv
from utils.DataBaseParser import DataBaseParser
from datetime import datetime

from utils.ErrorHandler import ErrorHandler
from utils.Requester import Requester

load_dotenv()


class Parser(Requester, ErrorHandler):
    def __init__(self, url, brand_id):
        super().__init__()
        self.url = url
        self.brand_id = brand_id
        self.max_page = self.get_max_page()
        self.cars_from_page = None
        self.get_cars()

    def get_max_page(self):
        response = self.request_get_max_page(url=self.url, brand_id=self.brand_id)
        if response.status_code == 200:
            response_json = response.json()
            return response_json['pageCount'] if response_json['pageCount'] <= 120 else 120
        return None

    def get_cars(self):
        try:
            for page in range(1, self.max_page + 1 if self.max_page > 1 else 2):
                sleep(0.6)
                response = self.request_get_cars(url=self.url, page=page, brand_id=self.brand_id, sort=4)
                if response.status_code == 200:
                    self.collect_cars(data=response.json())
                else:
                    if not self.max_page == 1:
                        self.error_logging(msg=response.json(), method='get_cars(35)')
                print(f"Страница {page} из {self.max_page}")

            if self.max_page == 120:
                for page in range(1, self.max_page + 1 if self.max_page > 1 else 2):
                    response = self.request_get_cars(url=self.url, page=page, brand_id=self.brand_id, sort=5)
                    if response.status_code == 200:
                        self.collect_cars(data=response.json())
                    else:
                        if not self.max_page == 1:
                            self.error_logging(msg=response.json(), method='get_cars(45)')
                    print(f"Страница {page} из {self.max_page} реверс")

        except Exception as e:
            self.error_logging(msg=e, method='get_cars(49)')

    def collect_cars(self, data):

        for car in data['adverts']:
            try:
                file_exist = DataBaseParser(car=car, phones=[], url=self.url).check_exist_car()
                if not file_exist:
                    DataBaseParser(car=car, phones=self.get_seller_phone(car['id']), url=self.url).save()
            except Exception as e:
                self.error_logging(msg=e, method='collect_cars(59)')

    def get_seller_phone(self, car_id):
        request = self.request_get_phone(car_id=car_id)
        if request.status_code == 200:
            phones = request.json()
            phones_list = []
            for i in phones[:2]:
                phones_list.append(i['country']['code'] + i['number'])
            return phones_list
        return ['ошибка при получении']
