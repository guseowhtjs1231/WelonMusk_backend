from django.views import View
from django.http  import JsonResponse
from .models      import CarModels, CarTypes, CarTypePrices, CarColors
from .models      import CarInteriors, CarInteriorPrices

class PriceView(View):
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)
            type_list = [
            {
                'model_name'  : cars.model_name ,
                'basic_price' : car['basic_price'],
                'model_type'  : CarTypes.objects.get(id=car['type_id']).model_type
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
                'img_url'     : CarColors.objects.get(id=car['color_id']).img_url
            } for car in list(cars.carcolorprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':color_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class InteriorPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carinteriorprices_set').get(id=model_id)
            interior_list = [
            {
                'interior_id'      : car['interior_id'],
                'interior_price'   : round(car['interior_price'],0),
                'interior_en_name' : CarInteriors.objects.get(id=car['interior_id']).interior_en_name,
                'interior_ko_name' : CarInteriors.objects.get(id=car['interior_id']).interior_ko_name,
                'img_url'          : CarInteriors.objects.get(id=car['interior_id']).img_url,
                'descriptions'     : car['descriptions']
            } for car in list(cars.carinteriorprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':interior_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)
