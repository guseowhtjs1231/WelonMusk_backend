from .models      import CarModels, CarTypes, CarTypePrices
from django.views import View
from django.http  import JsonResponse


class PriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)
            type_list = list(cars.car_models.all().values('type_id','basic_price'))

            for i in range(0, len(type_list)):
                car_type = CarTypes.objects.get(id=type_list[i]['type_id'])
                type_list[i]['model_type'] = car_type.model_type
                del type_list[i]['type_id']

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)
