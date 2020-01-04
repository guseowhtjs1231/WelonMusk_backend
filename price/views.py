from django.views import View
from django.http  import JsonResponse
from .models      import CarModels, CarTypes, CarTypePrices, CarColors
from .models      import CarSeats
from .models      import CarWheels
from .models      import CarInteriors, CarInteriorPrices
from .models      import CarOrderPrices

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

class TotalPriceView(View):
    SAVING_COST = 6800000
    def get(self, request, model_id):
        total_price = 0
        order = CarOrderPrices.objects.get(id=model_id)
        cars = CarModels.objects.prefetch_related('cartypeprices_set').get(id=model_id)
        basic_price = list(cars.cartypeprices_set.filter(type=order.type.id).values('basic_price'))[0]['basic_price']
        total_price += basic_price

        car_color = CarColors.objects.prefetch_related('carcolorprices_set').get(id=order.color.id)
        color_price = list( car_color.carcolorprices_set.filter(model=model_id).values('color_price'))[0]['color_price']
        total_price += color_price

        car_wheel = CarWheels.objects.prefetch_related('carwheelprices_set').get(id=order.wheel.id)
        wheel_price = list( car_wheel.carwheelprices_set.filter(model=model_id).values('wheel_price'))[0]['wheel_price']
        total_price += wheel_price

        car_interior = CarInteriors.objects.prefetch_related('carinteriorprices_set').get(id=order.interior.id)
        interior_price = list( car_interior.carinteriorprices_set.filter(model=model_id).values('interior_price'))[0]['interior_price']
        total_price += interior_price
        
        autopilot_price = order.autopilot_price.autopilot_price
        total_price += autopilot_price

        order.expected_price = total_price
        order.saving_price = total_price - TotalPriceView.SAVING_COST
        order.save()

        prices = {
            'expected_price' : round(order.expected_price, 0),
            'saving_price' : round(order.saving_price, 0),
        }

        return JsonResponse({'message':'SUCCESS', 'price':prices}, status=200)

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

class CarSeatPrice(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carseatprices_set').get(id=model_id)
            seat_list = [
            {
                'model_name' : car.model.model_name,
                'seat_id'    : car.seat.id,
                'seat_name'  : car.seat.seat_name,
                'seat_price' : round(car.seat_price, 0)
            } for car in list(cars.carseatprices_set.all())]

            return JsonResponse({'message':'SUCCESS','data':seat_list}, status=200)
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
