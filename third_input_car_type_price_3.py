import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *
from decimal import *


model_s = CarModels.objects.get(model_name='Model S')
model_3 = CarModels.objects.get(model_name='Model 3')
model_x = CarModels.objects.get(model_name='Model X')


standard_range_plus = CarTypes.objects.get(model_type='Standard Range Plus')
long_range = CarTypes.objects.get(model_type='Long Range')
performance = CarTypes.objects.get(model_type='Performance')

model_s_long_range_acceleration = 4.6
model_s_long_range_fuel_economy = 446
model_s_long_range_max_speed = 233
model_s_long_range_wheel = "<div>18인치 에어로 휠</div><div>19인치 스포츠 휠</div>"
model_s_long_range_included_options = "<div>프리미엄 인테리어</div>"

model_s_standard_range_plus_acceleration = 5.6
model_s_standard_range_plus_fuel_economy = 352
model_s_standard_range_plus_max_speed = 225
model_s_standard_range_plus_wheel = "<div>18인치 에어로 휠</div><div>19인치 스포츠 휠</div>"
model_s_standard_range_plus_included_options = "<div>부분 프리미엄 인테리어</div>"


model_3_standard_range_plus_acceleration = 5.6
model_3_standard_range_plus_fuel_economy = 352
model_3_standard_range_plus_max_speed = 225
model_3_standard_range_plus_wheel = "<div>18인치 에어로 휠</div><div>19인치 스포츠 휠</div>"
model_3_standard_range_plus_included_options = "<div>부분 프리미엄 인테리어</div>"
model_3_standard_range_plus_img_url = "https://static-assets.tesla.com/configurator/compositor?&options=$W38B,$PPSW,$DV2W,$MT308,$IN3B2&view=STUD_3QTR&model=m3&size=1441&bkba_opt=1&version=v0027d201912301150&version=v0027d201912301150"

model_3_long_range_acceleration = 4.6
model_3_long_range_fuel_economy = 446
model_3_long_range_max_speed = 233
model_3_long_range_wheel = "<div>18인치 에어로 휠</div><div>19인치 스포츠 휠</div>"
model_3_long_range_included_options = "<div>프리미엄 인테리어</div>"
model_3_long_range_img_url = "https://static-assets.tesla.com/configurator/compositor?&options=$W38B,$PPSW,$DV4W,$MT310,$IN3PB&view=STUD_3QTR&model=m3&size=1441&bkba_opt=1&version=v0027d201912301150&version=v0027d201912301150"

model_3_performance_acceleration = 3.4
model_3_performance_fuel_economy = 415
model_3_performance_max_speed = 261
model_3_performance_wheel = "<div>20인치 퍼포먼스 휠</div>"
model_3_performance_included_options = "<div>프리미엄 인테리어</div>"
model_3_performance_img_url = "https://static-assets.tesla.com/configurator/compositor?&options=$W32D,$PPSW,$DV4W,$SLR1,$MT311,$IN3PB&view=STUD_3QTR&model=m3&size=1441&bkba_opt=1&version=v0027d201912301150&version=v0027d201912301150"

model_x_long_range_acceleration = 4.6
model_x_long_range_fuel_economy = 446
model_x_long_range_max_speed = 233
model_x_long_range_wheel = "<div>18인치 에어로 휠</div><div>19인치 스포츠 휠</div>"
model_x_long_range_included_options = "<div>프리미엄 인테리어</div>"

model_x_performance_acceleration = 5.6
model_x_performance_fuel_economy = 352
model_x_performance_max_speed = 225
model_x_performance_wheel = "<div>18인치 에어로 휠</div><div>19인치 스포츠 휠</div>"
model_x_performance_included_options = "<div>부분 프리미엄 인테리어</div>"


CarTypePrices.objects.create(model = model_s, type = long_range, basic_price = 113600000, acceleration = model_s_long_range_acceleration, fuel_economy=model_s_long_range_fuel_economy,max_speed=model_s_long_range_max_speed, wheel=model_s_long_range_wheel, included_options=model_s_long_range_included_options, img_url = model_3_standard_range_plus_img_url)
CarTypePrices.objects.create(model = model_s, type = performance, basic_price = 138600000, acceleration = model_s_standard_range_plus_acceleration, fuel_economy=model_s_standard_range_plus_fuel_economy,max_speed=model_s_standard_range_plus_max_speed, wheel=model_s_standard_range_plus_wheel, included_options=model_s_standard_range_plus_included_options, img_url = model_3_standard_range_plus_img_url)

CarTypePrices.objects.create(model = model_3, type = standard_range_plus, basic_price = 53690000, acceleration = model_3_standard_range_plus_acceleration, fuel_economy=model_3_standard_range_plus_fuel_economy,max_speed=model_3_standard_range_plus_max_speed, wheel=model_3_standard_range_plus_wheel, included_options=model_3_standard_range_plus_included_options, img_url = model_3_standard_range_plus_img_url)
CarTypePrices.objects.create(model = model_3, type = long_range, basic_price = 63690000, acceleration = model_3_long_range_acceleration, fuel_economy=model_3_long_range_fuel_economy,max_speed=model_3_long_range_max_speed, wheel=model_3_long_range_wheel, included_options=model_3_long_range_included_options, img_url=model_3_standard_range_plus_img_url)
CarTypePrices.objects.create(model = model_3, type = performance, basic_price = 73690000, acceleration = model_3_performance_acceleration, fuel_economy=model_3_performance_fuel_economy,max_speed=model_3_performance_max_speed, wheel=model_3_performance_wheel, included_options=model_3_performance_included_options, img_url=model_3_standard_range_plus_img_url)


CarTypePrices.objects.create(model = model_x, type = long_range, basic_price = 121600000, acceleration = model_x_long_range_acceleration, fuel_economy=model_x_long_range_fuel_economy,max_speed=model_x_long_range_max_speed, wheel=model_x_long_range_wheel, included_options=model_x_long_range_included_options, img_url=model_3_standard_range_plus_img_url)
CarTypePrices.objects.create(model = model_x, type = performance, basic_price = 141600000, acceleration = model_x_performance_acceleration, fuel_economy=model_x_performance_fuel_economy,max_speed=model_x_performance_max_speed, wheel=model_x_performance_wheel, included_options=model_x_performance_included_options, img_url=model_3_standard_range_plus_img_url)
