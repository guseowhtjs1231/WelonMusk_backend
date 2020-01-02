import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *
from decimal import *


model_s = CarModels.objects.get(model_name='Model S')
model_3 = CarModels.objects.get(model_name='Model 3')
model_x = CarModels.objects.get(model_name='Model X')


number_5_seats = CarSeats.objects.get(seat_name='5개 시트 구성')
number_6_seats = CarSeats.objects.get(seat_name='6개 시트 구성')
number_7_seats = CarSeats.objects.get(seat_name='7개 시트 구성')


CarSeatPrices.objects.create(model=model_x, seat=number_5_seats, seat_price = 0)
CarSeatPrices.objects.create(model=model_x, seat=number_6_seats, seat_price = 8525000)
CarSeatPrices.objects.create(model=model_x, seat=number_7_seats, seat_price = 4590000)
