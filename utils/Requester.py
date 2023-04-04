from utils.GenerateHeaders import GenerateHeaders
from utils.ErrorHandler import ErrorHandler
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Requester(GenerateHeaders, ErrorHandler):

    def request_get_max_page(self, url, brand_id):
        body = {'page': 1,
                'properties': [{'name': 'brands', 'property': 6, 'value': [[{'name': 'brand', 'value': brand_id}]]},
                               {'name': 'price_currency', 'value': 2}]
                }
        return requests.post(url=url, json=body, headers=self.generate_headers())

    def request_get_cars(self, url, brand_id, page, sort):
        body = {'page': page,
                'properties': [
                    {'name': 'brands', 'property': 6, 'value': [[{'name': 'brand', 'value': brand_id}]]},
                    {'name': 'price_currency', 'value': 2}],
                'sorting': sort
                }
        return requests.post(url=url, json=body, headers=self.generate_headers())

    def request_get_phone(self, car_id):
        url = f"{os.environ.get('PHONE_URL')}{car_id}/phones"
        return requests.get(url=url, headers=self.generate_headers())

    def request_check_car_status(self, car_id):
        url = f"{os.environ.get('ONE_CAR_URL')}{car_id}"
        request = requests.get(url=url, headers=self.generate_headers())
        if request.status_code == 200:
            return request.json()['publicStatus']['label']
        elif request.status_code == 404:
            return 'delete'
        else:
            self.error_logging(msg=request.json(),
                               method=f'request_check_car_status(38) status_code={request.status_code}')

    def request_get_vin_car(self, event_id, headers):
        try:
            url = f"{os.environ.get('CHECK_VIN_URL_CARS')}{event_id}/vin"
            request = requests.get(url=url, headers=headers)
            if request.status_code == 200:
                request_json = request.json()
                return request_json['vin']
            else:
                return None
        except Exception as e:
            self.error_logging(msg=e, method='request_get_vin_car(53)')

    def request_get_vin_truck(self, event_id, headers):
        try:
            url = f"{os.environ.get('CHECK_VIN_URL_TRUCK')}{event_id}/vin"
            request = requests.get(url=url, headers=headers)
            print(url)
            print(request.json())
            if request.status_code == 200:
                request_json = request.json()
                return request_json['vin']
            else:
                return None
        except Exception as e:
            self.error_logging(msg=e, method='request_get_vin_car(53)')

