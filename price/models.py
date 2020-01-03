from django.db import models

class CarModels(models.Model):
    model_name = models.CharField(max_length = 50)
    car_types = models.ManyToManyField('CarTypes', through ='CarTypePrices', related_name='car_models')
    car_colors = models.ManyToManyField('CarColors', through ='CarColorPrices')
    car_wheels = models.ManyToManyField('CarWheels', through ='CarWheelPrices')

    class Meta:
        db_table = 'car_models'

class CarTypes(models.Model):
    model_type = models.CharField(max_length = 50)

    class Meta:
        db_table = 'car_types'

class CarTypePrices(models.Model):
    model = models.ForeignKey('CarModels', related_name='car_models', on_delete= models.SET_NULL, null=True)
    type = models.ForeignKey('CarTypes', related_name='car_types', on_delete= models.SET_NULL, null=True)
    basic_price = models.DecimalField(max_digits = 19, decimal_places = 2)

    class Meta:
        db_table = 'car_type_prices'

class CarColors(models.Model):
    color_name = models.CharField(max_length = 50)
    img_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'car_colors'

class CarColorPrices(models.Model):
    model = models.ForeignKey('CarModels', on_delete = models.SET_NULL, null=True)
    color = models.ForeignKey('CarColors', on_delete = models.SET_NULL, null=True)
    color_price = models.DecimalField(max_digits = 12, decimal_places = 2)

    class Meta:
        db_table = 'car_color_prices'

class CarWheels(models.Model):
    wheel_name = models.CharField(max_length = 50)
    img_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'car_wheels'

class CarWheelPrices(models.Model):
    model = models.ForeignKey('CarModels', on_delete = models.SET_NULL, null=True)
    wheel = models.ForeignKey('CarWheels', on_delete = models.SET_NULL, null=True)
    wheel_price = models.DecimalField(max_digits = 12, decimal_places = 2)

    class Meta:
        db_table = 'car_wheel_prices'

class CarInteriors(models.Model):
    interior_en_name = models.CharField(max_length = 50)
    interior_ko_name = models.CharField(max_length = 50)
    img_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'car_interiors'
