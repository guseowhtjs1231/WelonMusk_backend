from django.db import models

class CarModels(models.Model):
    model_name = models.CharField(max_length = 50)
    car_types = models.ManyToManyField('CarTypes', through ='CarTypePrices', related_name='car_models')

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
