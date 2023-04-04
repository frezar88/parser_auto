from config.db import meta, engine
from .cars_model import cars_model
from .car_options_model import cars_options_model
from .trucks_model import trucks_model
from .trucks_options_model import trucks_options_model
from .status_change import status_change_model

meta.create_all(bind=engine)

