import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *
from decimal import *


model_s = CarModels.objects.get(model_name='Model S')
model_3 = CarModels.objects.get(model_name='Model 3')
model_x = CarModels.objects.get(model_name='Model X')


inch_19_silver = CarWheels.objects.get(wheel_name='19인치 실버 휠')
inch_19_sonic_cabon = CarWheels.objects.get(wheel_name='19인치 소닉 카본 슬립스트림 휠')
inch_21_sonic_cabon = CarWheels.objects.get(wheel_name='21인치 소닉 카본 트윈 터빈 휠')
inch_18_aero = CarWheels.objects.get(wheel_name='18인치 에어로 휠')
inch_19_sports = CarWheels.objects.get(wheel_name='19인치 스포츠 휠')
inch_20_silver = CarWheels.objects.get(wheel_name='20인치 실버 휠')
inch_20_two_tones = CarWheels.objects.get(wheel_name='20인치 투톤 슬립스트림 휠')
inch_22_onics_black = CarWheels.objects.get(wheel_name='22인치 오닉스 블랙 휠')

CarWheelPrices.objects.create(model = model_s, wheel = inch_19_silver, wheel_price= 0)
CarWheelPrices.objects.create(model = model_s, wheel = inch_19_sonic_cabon, wheel_price= 1968000)
CarWheelPrices.objects.create(model = model_s, wheel = inch_21_sonic_cabon, wheel_price= 5902000)


CarWheelPrices.objects.create(model = model_3, wheel = inch_18_aero, wheel_price= 0)
CarWheelPrices.objects.create(model = model_3, wheel = inch_19_sports, wheel_price= 1929000)


CarWheelPrices.objects.create(model = model_x, wheel = inch_20_silver, wheel_price= 0)
CarWheelPrices.objects.create(model = model_x, wheel = inch_20_two_tones, wheel_price= 2624000)
CarWheelPrices.objects.create(model = model_x, wheel = inch_22_onics_black, wheel_price= 7213000)
