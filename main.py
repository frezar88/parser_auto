import ast
from dotenv import load_dotenv
import os
from utils.Parser import Parser
load_dotenv()

if __name__ == '__main__':
    try:
        cars = ast.literal_eval(os.environ.get('BRAND_CAR_DICT'))
        for brand in cars:
            print(brand)
            Parser(url=os.environ.get('CARS_URL'), brand_id=cars[brand])
        truck = ast.literal_eval(os.environ.get('BRAND_TRUCK_DICT'))
        for brand in truck:
            print(brand)
            Parser(url=os.environ.get('TRACK_URL'), brand_id=truck[brand])
    except KeyboardInterrupt:
        print('Принудительное завершение работы программы.')


