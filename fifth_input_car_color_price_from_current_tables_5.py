import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "welonmusk.settings")
import django
django.setup()

from price.models import *
from decimal import *


model_s = CarModels.objects.get(model_name='Model S')
model_3 = CarModels.objects.get(model_name='Model 3')
model_x = CarModels.objects.get(model_name='Model X')


pearl_white_multi_coat = CarColors.objects.get(color_name='Pearl White Multi-Coat')
solid_black = CarColors.objects.get(color_name='Solid Black')
midnight_silver_metallic = CarColors.objects.get(color_name='Midnight Silver Metallic')
deep_blue_metallic = CarColors.objects.get(color_name='Deep Blue Metallic')
red_multi_coat = CarColors.objects.get(color_name='Red Multi-Coat')

CarColorPrices.objects.create(model = model_s, color = pearl_white_multi_coat, color_price= 0)
CarColorPrices.objects.create(model = model_s, color = solid_black, color_price= 1968000)
CarColorPrices.objects.create(model = model_s, color = midnight_silver_metallic, color_price= 1968000)
CarColorPrices.objects.create(model = model_s, color = deep_blue_metallic, color_price= 1968000)
CarColorPrices.objects.create(model = model_s, color = red_multi_coat, color_price= 3279000)


CarColorPrices.objects.create(model = model_3, color = pearl_white_multi_coat, color_price= 0)
CarColorPrices.objects.create(model = model_3, color = solid_black, color_price= 1286000)
CarColorPrices.objects.create(model = model_3, color = midnight_silver_metallic, color_price= 1286000)
CarColorPrices.objects.create(model = model_3, color = deep_blue_metallic, color_price= 1286000)
CarColorPrices.objects.create(model = model_3, color = red_multi_coat, color_price= 2571000)


CarColorPrices.objects.create(model = model_x, color = pearl_white_multi_coat, color_price= 0)
CarColorPrices.objects.create(model = model_x, color = solid_black, color_price= 1968000)
CarColorPrices.objects.create(model = model_x, color = midnight_silver_metallic, color_price= 1968000)
CarColorPrices.objects.create(model = model_x, color = deep_blue_metallic, color_price= 1968000)
CarColorPrices.objects.create(model = model_x, color = red_multi_coat, color_price= 3279000)
