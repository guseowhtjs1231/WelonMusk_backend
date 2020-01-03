import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *
from decimal import *


model_s = CarModels.objects.get(model_name='Model S')
model_3 = CarModels.objects.get(model_name='Model 3')
model_x = CarModels.objects.get(model_name='Model X')

default_payment = CarPaymentOptions.objects.get(id=1) # cash

default_model_s_type = CarTypes.objects.get(id=2) # Long Range
default_model_3_type = CarTypes.objects.get(id=1) # Standard Range Plus
default_model_x_type = CarTypes.objects.get(id=2) # Long Range

default_color_model_s_3_x = CarColors.objects.get(color_name='Pearl White Multi-Coat')



default_wheel_model_s_inch_19_silver = CarWheels.objects.get(wheel_name='19인치 실버 휠')
default_wheel_model_3_inch_18_aero = CarWheels.objects.get(wheel_name='18인치 에어로 휠')
default_wheel_model_x_inch_20_silver = CarWheels.objects.get(wheel_name='20인치 실버 휠')


default_interior_model_s_ash_wood_deco = CarInteriors.objects.get(id=1)
default_interior_model_3_1_all_black = CarInteriors.objects.get(id=6)
default_interior_model_x_1_all_black = CarInteriors.objects.get(id=8)


default_seat_model_x_number_5_seats = CarSeats.objects.get(seat_name='5개 시트 구성')


default_autopilot_price = CarAutoPilots.objects.get(id=1)


default_model_s_expected_price = 113600000
default_model_s_saving_price = 106800000

default_model_3_expected_price = 53690000
default_model_3_saving_price = 48690000

default_model_x_expected_price = 121600000
default_model_x_saving_price = 115200000

CarOrderPrices.objects.create(model = model_s, type = default_model_s_type, color = default_color_model_s_3_x, payment= default_payment,wheel= default_wheel_model_s_inch_19_silver, interior=default_interior_model_s_ash_wood_deco , seat = None, autopilot_price = default_autopilot_price, expected_price=default_model_s_expected_price, saving_price=default_model_s_saving_price)
CarOrderPrices.objects.create(model = model_3, type = default_model_3_type, color = default_color_model_s_3_x, payment= default_payment,wheel= default_wheel_model_3_inch_18_aero , interior=default_interior_model_3_1_all_black , seat = None, autopilot_price = default_autopilot_price, expected_price=default_model_3_expected_price, saving_price=default_model_3_saving_price)
CarOrderPrices.objects.create(model = model_x, type = default_model_x_type, color = default_color_model_s_3_x, payment= default_payment,wheel= default_wheel_model_x_inch_20_silver , interior=default_interior_model_x_1_all_black , seat = default_seat_model_x_number_5_seats, autopilot_price = default_autopilot_price, expected_price=default_model_x_expected_price, saving_price=default_model_x_saving_price)
