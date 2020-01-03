import json
from .models      import CarModels, CarTypes, CarTypePrices, CarColors, CarWheels
from .models      import CarInteriors, CarInteriorPrices
from .models      import CarOrderPrices
from .models      import CarSeats
from .models      import CarPaymentOptions
from .models      import CarAutoPilots

from django.views import View
from django.http  import JsonResponse

class PriceView(View):
    SAVING_COST = 6800000
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)

            type_list = [
            {
                'model_name' : cars.model_name ,
                'basic_price' : round(car['basic_price'],0),
                'type_id' : car['type_id'],
                'model_type' : CarTypes.objects.get(id=car['type_id']).model_type,
                'fuel_economy' : car['fuel_economy'],
                'max_speed' : car['max_speed'],
                'acceleration' : car['acceleration'],
                'img_url' : car['img_url']
            } for car in list(cars.car_models.all().values())]

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class TotalPriceView(View):

    def get(self, request, model_id):
        total_price = 0
        order = CarOrderPrices.objects.get(id=model_id)
        cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)
        basic_price = list(cars.car_models.filter(type=order.type.id).values('basic_price'))[0]['basic_price']
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
        order.saving_price = total_price - PriceView.SAVING_COST
        order.save()

        prices = {
            'expected_price' : round(order.expected_price, 0),
            'saving_price' : round(order.saving_price, 0),
        }

        return JsonResponse({'message':'SUCCESS', 'price':prices}, status=200)


class CarTypeView(View):
    def post(self, request, model_id):
        data = json.loads(request.body)

        if "type_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.type = CarTypes.objects.get(id=data['type_id'])
            order.save()
        else:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)


class ColorPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carcolorprices_set').get(id=model_id)

            color_list = [
            {
                'model_name' : cars.model_name,
                'color_id' : car['color_id'],
                'color_price' : round(car['color_price'], 0),
                'color_name' : CarColors.objects.get(id=car['color_id']).color_name,
                'img_url' : CarColors.objects.get(id=car['color_id']).img_url,
            } for car in list(cars.carcolorprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':color_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if "color_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.color = CarColors.objects.get(id=data['color_id'])
            order.save()
        else:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)

class WheelPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carwheelprices_set').get(id=model_id)

            type_list = [
            {
                'wheel_id' : car['wheel_id'], #'interior_id' : car['interior_id']
                'wheel_name' : CarWheels.objects.get(id=car['wheel_id']).wheel_name,
                'img_url' : CarWheels.objects.get(id=car['wheel_id']).img_url,
                'wheel_price' : round(car['wheel_price'], 0)
            } for car in list(cars.carwheelprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if "wheel_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.wheel = CarWheels.objects.get(id=data['wheel_id'])
            order.save()
        else:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)


class InteriorPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carinteriorprices_set').get(id=model_id)

            interior_list = [
            {
                'interior_id' : car['interior_id'],
                'interior_price' : round(car['interior_price'],0),
                'interior_en_name' : CarInteriors.objects.get(id=car['interior_id']).interior_en_name,
                'interior_ko_name' : CarInteriors.objects.get(id=car['interior_id']).interior_ko_name,
                'img_url' : CarInteriors.objects.get(id=car['interior_id']).img_url,
                'descriptions' : car['descriptions']
            } for car in list(cars.carinteriorprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':interior_list}, status=200)
        
        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if "interior_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.interior = CarInteriors.objects.get(id=data['interior_id'])
            order.save()
        else:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)


class SpecificationView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)
            type_list = [
            {
                'model_name' : cars.model_name ,
                'model_type' : CarTypes.objects.get(id=car['type_id']).model_type,
                'acceleration' : car['acceleration'],
                'fuel_economy' : car['fuel_economy'],
                'max_speed' : car['max_speed'],
                'wheel' : car['wheel'],
                'included_options' : car['included_options']
            } for car in list(cars.car_models.all().values())]

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class CarSeatPrice(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carseatprices_set').get(id=model_id)
            type_list = [
            {
                'model_name' : cars.model_name ,
                'seat_id' : car['seat_id'],
                'seat_name' : CarSeats.objects.get(id=car['seat_id']).seat_name,
                'seat_price' : round(car['seat_price'], 0)
            } for car in list(cars.carseatprices_set.all().values())]

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class CarPaymentOptionView(View):

    def get(self, request, model_id):
        try:
            order = CarOrderPrices.objects.get(id=model_id)
            if order.payment.option != 'cash':
                prices = {
                    'monthly_cost' : round(order.expected_price/order.payment.month, 0),
                    'saving_cost' : round(order.saving_price/order.payment.month, 0)
                }
                return JsonResponse({'message':'SUCCESS', 'data':prices}, status=200)
            else:
                return JsonResponse({'message':'NOT_SUPPORTED_FOR_CASH'}, status = 400)
        
        except ZeroDivisionError:
            return JsonResponse({'message':'SELECT_PAYMENTOPTION_FIRST'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if 'option' in data and 'month' in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.payment = CarPaymentOptions.objects.filter(option=data['option']).get(month=data['month'])
            order.save()
        else:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)


        return JsonResponse({'message':'SUCCESS'}, status=200)

class CarAutoPilotView(View):

    def post(self, request, model_id):
        data = json.loads(request.body)

        if 'autopilot' in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.autopilot_price = CarAutoPilots.objects.get(id = 2 if data['autopilot'] == 'True' else 1)
            order.save()
        else:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)
