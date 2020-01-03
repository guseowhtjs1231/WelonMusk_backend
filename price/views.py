from django.views import View
from django.http  import JsonResponse
from .models      import CarModels, CarTypes, CarTypePrices, CarColors
from .models      import CarWheels
from .models      import CarInteriors, CarInteriorPrices

class PriceView(View):
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('cartypeprices_set').get(id=model_id)
            type_list = [
            {
                'model_name'  : car.model.model_name,
                'basic_price' : car.basic_price,
                'model_type'  : car.type.model_type,
            } for car in list(cars.cartypeprices_set.all())]

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class ColorPriceView(View):
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carcolorprices_set').get(id=model_id)
            color_list = [
            {
                'model_name'  : car.model.model_name,
                'color_id'    : car.color.id,
                'color_price' : car.color_price,
                'color_name'  : car.color.color_name,
                'img_url'     : car.color.img_url,
            } for car in list(cars.carcolorprices_set.all())]

            return JsonResponse({'message':'SUCCESS','data':color_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class WheelPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carwheelprices_set').get(id=model_id)
            wheel_list = [
            {
                'wheel_id'    : car.wheel_id,
                'wheel_name'  : car.wheel.wheel_name,
                'img_url'     : car.wheel.img_url,
                'wheel_price' : round(car.wheel_price, 0)
            } for car in list(cars.carwheelprices_set.all())]

            return JsonResponse({'message':'SUCCESS','data':wheel_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class InteriorPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carinteriorprices_set').get(id=model_id)
            interior_list = [
            {
                'interior_id'      : car.interior_id,
                'interior_price'   : round(car.interior_price,0),
                'interior_en_name' : car.interior.interior_en_name,
                'interior_ko_name' : car.interior.interior_ko_name,
                'img_url'          : car.interior.img_url,
                'descriptions'     : car.descriptions
            } for car in list(cars.carinteriorprices_set.all())]

            return JsonResponse({'message':'SUCCESS','data':interior_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)
