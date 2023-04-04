from datetime import datetime
from utils.DataBase import DataBase
from dotenv import load_dotenv
from models.cars_model import cars_model
from models.car_options_model import cars_options_model
from models.trucks_model import trucks_model
from models.trucks_options_model import trucks_options_model
import os

load_dotenv()


class DataBaseParser(DataBase):
    def __init__(self, car, phones, url):
        super().__init__()
        self.car = car
        self.phones = phones
        self.url = url

    def helper_cars(self, field_name):
        data = list(filter(lambda item: item['name'] == field_name, self.car['properties']))
        if len(data):
            if data[0]['value'] == 'true':
                return True
            return data[0]['value']
        return None

    def helper_cars_options(self, field_name):
        data = list(filter(lambda item: item['name'] == field_name, self.car['properties']))
        if len(data):
            if data[0]['value'] == 'true':
                return True
            return data[0]['value']
        return False

    def save_truck(self):
        truck = self.data_base.execute(trucks_model.insert().values(
            event_id=self.car['id'],
            is_vin=True if len(self.car['metadata']) and self.car['metadata'].get('vinInfo') else False,
            status=self.car['publicStatus']['label'],
            public_url=self.car['publicUrl'],
            brand=self.helper_cars('brand'),
            model=self.helper_cars('model'),
            year=self.car['year'],
            engine_capacity=self.helper_cars('engine_capacity'),
            engine_type=self.helper_cars('engine_type'),
            transmission_type=self.helper_cars('transmission_type'),
            modification=self.helper_cars('modification'),
            wheelFormula=self.helper_cars('wheelFormula'),
            minifiedType=self.helper_cars('minifiedType'),
            body_type=self.helper_cars('body_type'),
            mileage_km=self.helper_cars('mileageKm'),
            location_short=self.car['shortLocationName'],
            location_full=self.car['locationName'],
            price_usd=self.car['price']['usd']['amount'],
            price_byn=self.car['price']['byn']['amount'],
            price_rub=self.car['price']['rub']['amount'],
            price_eur=self.car['price']['eur']['amount'],
            seller_phone=self.phones[0],
            seller_phone2=self.phones[1] if len(self.phones) == 2 else None,
            seller_name=self.car['sellerName'],
            exchange=self.car['exchange']['label'],
            car_description=self.car['description'] if self.car.get('description') else '',
            published_at=datetime.strptime(self.car['publishedAt'], "%Y-%m-%dT%H:%M:%S%z"),
            refreshed_at=datetime.strptime(self.car['refreshedAt'], "%Y-%m-%dT%H:%M:%S%z")
            if self.car.get('refreshedAt')
            else None,
            renewed_at=datetime.strptime(self.car['renewedAt'], "%Y-%m-%dT%H:%M:%S%z")
            if self.car.get('renewedAt')
            else None,
            originalDaysOnSale=self.car['originalDaysOnSale'],
        ))
        self.save_truck_option(truck.lastrowid)

    def save_car(self):
        car = self.data_base.execute(cars_model.insert().values(
            event_id=self.car['id'],
            is_vin=True if self.car['metadata'].get('vinInfo') else False,
            status=self.car['publicStatus']['label'],
            public_url=self.car['publicUrl'],
            brand=self.helper_cars('brand'),
            model=self.helper_cars('model'),
            year=self.car['year'],
            engine_capacity=self.helper_cars('engine_capacity'),
            engine_type=self.helper_cars('engine_type'),
            transmission_type=self.helper_cars('transmission_type'),
            generation=self.helper_cars('generation'),
            body_type=self.helper_cars('body_type'),
            drive_type=self.helper_cars('drive_type'),
            color=self.helper_cars('color'),
            mileage_km=self.helper_cars('mileage_km'),
            location_short=self.car['shortLocationName'],
            location_full=self.car['locationName'],
            price_usd=self.car['price']['usd']['amount'],
            price_byn=self.car['price']['byn']['amount'],
            price_rub=self.car['price']['rub']['amount'],
            price_eur=self.car['price']['eur']['amount'],
            seller_phone=self.phones[0],
            seller_phone2=self.phones[1] if len(self.phones) == 2 else None,
            seller_name=self.car['sellerName'],
            exchange=self.car['exchange']['label'],
            car_description=self.car['description'] if self.car.get('description') else '',
            interior_color=self.helper_cars('interior_color'),
            interior_material=self.helper_cars('interior_material'),
            published_at=datetime.strptime(self.car['publishedAt'], "%Y-%m-%dT%H:%M:%S%z"),
            refreshed_at=datetime.strptime(self.car['refreshedAt'], "%Y-%m-%dT%H:%M:%S%z")
            if self.car.get('refreshedAt')
            else None,
            renewed_at=datetime.strptime(self.car['renewedAt'], "%Y-%m-%dT%H:%M:%S%z")
            if self.car.get('renewedAt')
            else None,
            originalDaysOnSale=self.car['originalDaysOnSale'],
        ))
        self.save_car_option(car.lastrowid)

    def save_car_option(self, last_row_id, ):
        self.data_base.execute(cars_options_model.insert().values(
            cars_id=last_row_id,
            photo=self.car['photos'],
            abs=self.helper_cars_options('abs'),
            esp=self.helper_cars_options('esp'),
            anti_slip_system=self.helper_cars_options('anti_slip_system'),
            rain_detector=self.helper_cars_options('rain_detector'),
            rear_view_camera=self.helper_cars_options('rear_view_camera'),
            immobilizer=self.helper_cars_options('immobilizer'),
            alarm=self.helper_cars_options('alarm'),
            front_safebags=self.helper_cars_options('front_safebags'),
            side_safebags=self.helper_cars_options('side_safebags'),
            alloy_wheels=self.helper_cars_options('alloy_wheels'),
            rear_safebags=self.helper_cars_options('rear_safebags'),
            railings=self.helper_cars_options('railings'),
            parktronics=self.helper_cars_options('parktronics'),
            panoramic_roof=self.helper_cars_options('panoramic_roof'),
            cruise_control=self.helper_cars_options('cruise_control'),
            electro_seat_adjustment=self.helper_cars_options('electro_seat_adjustment'),
            steering_wheel_media_control=self.helper_cars_options('steering_wheel_media_control'),
            media_screen=self.helper_cars_options('media_screen'),
            navigator=self.helper_cars_options('navigator'),
            led_lights=self.helper_cars_options('led_lights'),
            climate_control=self.helper_cars_options('climate_control'),
            front_glass_lift=self.helper_cars_options('front_glass_lift'),
            seat_heating=self.helper_cars_options('seat_heating'),
            front_glass_heating=self.helper_cars_options('front_glass_heating'),
            mirror_heating=self.helper_cars_options('mirror_heating'),
            conditioner=self.helper_cars_options('conditioner'),
            aux_ipod=self.helper_cars_options('aux_ipod'),
            bluetooth=self.helper_cars_options('bluetooth'),
            cd_mp3_player=self.helper_cars_options('cd_mp3_player'),
            usb=self.helper_cars_options('usb'),
            fog_lights=self.helper_cars_options('fog_lights'),
            xenon_lights=self.helper_cars_options('xenon_lights'),
            hitch=self.helper_cars_options('hitch'),
        ))

    def save_truck_option(self, last_row_id):
        self.data_base.execute(trucks_options_model.insert().values(
            truck_id=last_row_id,
            photo=self.car['photos'],
            abs=self.helper_cars_options('abs'),
            heater=self.helper_cars_options('heater'),
            conditioner=self.helper_cars_options('conditioner'),
            cruise_control=self.helper_cars_options('cruise_control'),
            navigation=self.helper_cars_options('navigation'),
            mirror_heating=self.helper_cars_options('mirror_heating'),
            safety_bags=self.helper_cars_options('safety_bags'),
            berth=self.helper_cars_options('berth'),
            tachograph=self.helper_cars_options('tachograph'),
            central_locking=self.helper_cars_options('central_locking'),
            three_way_unloading=self.helper_cars_options('three_way_unloading'),
            side_unloading=self.helper_cars_options('side_unloading'),
            rear_unloading=self.helper_cars_options('rear_unloading'),
        ))

    def save(self):
        if self.url == os.environ.get('CARS_URL'):
            self.save_car()
        if self.url == os.environ.get('TRACK_URL'):
            self.save_truck()

    def check_exist_car(self, ):
        if self.url == os.environ.get('CARS_URL'):
            car = self.data_base.execute(cars_model.select().where(cars_model.c.event_id == self.car['id'])).fetchone()
            if car:
                return True
            else:
                return False
        if self.url == os.environ.get('TRACK_URL'):
            truck = self.data_base.execute(
                trucks_model.select().where(trucks_model.c.event_id == self.car['id'])).fetchone()
            if truck:
                return True
            else:
                return False
