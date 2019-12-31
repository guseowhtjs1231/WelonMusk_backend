from django.views import View
from django.http  import JsonResponse
from .models      import CarModels, CarTypes, CarTypePrices, CarColors

class PriceView(View):
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)
            type_list = [
            {
                'model_name' : cars.model_name ,
                'basic_price' : car['basic_price'],
                'model_type' : CarTypes.objects.get(id=car['type_id']).model_type,
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
                'model_name' : cars.model_name,
                'color_id' : CarColors.objects.get(id=car['color_id']).id,
                'color_price' : car['color_price'],
                'color_name' : CarColors.objects.get(id=car['color_id']).color_name,
                'img_url' : CarColors.objects.get(id=car['color_id']).img_url,
            } for car in list(cars.carcolorprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':color_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

