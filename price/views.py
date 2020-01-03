from django.views import View
from django.http  import JsonResponse
from .models      import CarModels, CarTypes, CarTypePrices, CarColors
from .models      import CarWheels

class PriceView(View):
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)
            type_list = [
            {
                'model_name'  : cars.model_name ,
                'basic_price' : car['basic_price'],
                'model_type'  : CarTypes.objects.get(id=car['type_id']).model_type,
            } for car in list(cars.car_models.all().values())]

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class ColorPriceView(View):
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carcolorprices_set').get(id=model_id)

            color_list = [
            {
                'model_name'  : cars.model_name,
                'color_id'    : CarColors.objects.get(id=car['color_id']).id,
                'color_price' : car['color_price'],
                'color_name'  : CarColors.objects.get(id=car['color_id']).color_name,
                'img_url'     : CarColors.objects.get(id=car['color_id']).img_url,
            } for car in list(cars.carcolorprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':color_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class WheelPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carwheelprices_set').get(id=model_id)
            wheel_list = [
            {
                'wheel_id'    : car['wheel_id'],
                'wheel_name'  : CarWheels.objects.get(id=car['wheel_id']).wheel_name,
                'img_url'     : CarWheels.objects.get(id=car['wheel_id']).img_url,
                'wheel_price' : round(car['wheel_price'], 0)
            } for car in list(cars.carwheelprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':wheel_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)
