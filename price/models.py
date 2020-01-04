from django.db import models

class CarModels(models.Model):
    model_name = models.CharField(max_length = 50)
    car_types = models.ManyToManyField('CarTypes', through ='CarTypePrices')
    car_colors = models.ManyToManyField('CarColors', through ='CarColorPrices')
    car_wheels = models.ManyToManyField('CarWheels', through ='CarWheelPrices')
    car_interior = models.ManyToManyField('CarInteriors', through='CarInteriorPrices')
    car_seats = models.ManyToManyField('CarSeats', through ='CarSeatPrices')

    class Meta:
        db_table = 'car_models'

class CarTypes(models.Model):
    model_type = models.CharField(max_length = 50)

    class Meta:
        db_table = 'car_types'

class CarTypePrices(models.Model):
    model = models.ForeignKey('CarModels', on_delete= models.SET_NULL, null=True)
    type = models.ForeignKey('CarTypes', on_delete= models.SET_NULL, null=True)
    basic_price = models.DecimalField(max_digits = 19, decimal_places = 2)
    acceleration = models.DecimalField(max_digits = 6, decimal_places = 1)
    fuel_economy = models.DecimalField(max_digits = 6, decimal_places = 0)
    max_speed = models.DecimalField(max_digits = 6, decimal_places = 0)
    wheel = models.CharField(max_length = 200)
    included_options = models.CharField(max_length = 200)
    img_url = models.URLField(max_length=2000)

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

class CarInteriorPrices(models.Model):
    model = models.ForeignKey('CarModels', on_delete = models.SET_NULL, null=True)
    interior = models.ForeignKey('CarInteriors', on_delete = models.SET_NULL, null=True)
    interior_price = models.DecimalField(max_digits = 12, decimal_places = 2)
    descriptions = models.CharField(max_length=3000)

    class Meta:
        db_table = 'car_interior_prices'

class CarSeats(models.Model):
    seat_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'car_seats'

class CarSeatPrices(models.Model):
    model = models.ForeignKey('CarModels', on_delete = models.SET_NULL, null=True)
    seat = models.ForeignKey('CarSeats', on_delete = models.SET_NULL, null=True)
    seat_price = models.DecimalField(max_digits = 20, decimal_places = 2)

    class Meta:
        db_table = 'car_seat_prices'

class CarOrderPrices(models.Model):
    model = models.ForeignKey('CarModels', on_delete = models.SET_NULL, null=True)
    type = models.ForeignKey('CarTypes', on_delete = models.SET_NULL, null=True)
    color = models.ForeignKey('CarColors', on_delete = models.SET_NULL, null=True)
    payment = models.ForeignKey('CarPaymentOptions', on_delete = models.SET_NULL, null=True)
    wheel = models.ForeignKey('CarWheels', on_delete = models.SET_NULL, null=True)
    interior = models.ForeignKey('CarInteriors', on_delete = models.SET_NULL, null=True)
    seat = models.ForeignKey('CarSeats', on_delete= models.SET_NULL, null=True)
    autopilot_price = models.ForeignKey('CarAutoPilots', on_delete= models.SET_NULL, null=True)

    expected_price = models.DecimalField(max_digits = 19, decimal_places = 2,null=True)
    saving_price = models.DecimalField(max_digits = 19, decimal_places = 2,null=True)

    class Meta:
        db_table = 'car_order_prices'

class CarAutoPilots(models.Model):
    autopilot_price = models.DecimalField(max_digits = 20, decimal_places = 2)

    class Meta:
        db_table = 'car_auto_pilot'

class CarPaymentOptions(models.Model):
    option = models.CharField(max_length=50)
    month = models.IntegerField()

    class Meta:
        db_table = 'car_payment_option'
