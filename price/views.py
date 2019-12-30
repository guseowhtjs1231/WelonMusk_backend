from django.views import View
from django.http  import JsonResponse
from .models      import CarModels, CarColors

class ColorPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carcolorprices_set').get(id=model_id)
            color_list = list(cars.carcolorprices_set.all().values('color_id','color_price'))

            for i in range(0, len(color_list)):
                car_color = CarColors.objects.get(id=color_list[i]['color_id'])
                color_list[i]['color_name'] = car_color.color_name
                color_list[i]['img_url'] = car_color.img_url
                del color_list[i]['color_id']

            return JsonResponse({'message':'SUCCESS','data':color_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)
