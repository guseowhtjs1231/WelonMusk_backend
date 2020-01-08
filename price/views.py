import json

from django.views import View
from django.http  import JsonResponse
from django.http  import HttpResponse

from .models      import (
    CarModels,
    CarTypes,
    CarTypePrices,
    CarColors,
    CarSeats,
    CarWheels,
    CarInteriors,
    CarInteriorPrices,
    CarOrderPrices,
    CarPaymentOptions,
    CarAutoPilots
)

class PriceView(View):
    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('cartypeprices_set').get(id=model_id)
            model_data = [
            {
                'model_name'    : car.model.model_name,
                'basic_price'   : round(car.basic_price, 0),
                'model_type'    : car.type.model_type,
                'type_id'       : car.type.id,
                'model_type'    : car.type.model_type,
                'fuel_economy'  : car.fuel_economy,
                'max_speed'     : car.max_speed,
                'acceleration'  : car.acceleration,
                'img_url'       : car.img_url
            } for car in list(cars.cartypeprices_set.all())]

            return JsonResponse({'data':model_data}, status=200)

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
            'saving_price'   : round(order.saving_price, 0),
        }

        return JsonResponse({'price':prices}, status=200)

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

            return JsonResponse({'data':color_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if "color_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.color = CarColors.objects.get(id=data['color_id'])
            order.save()
            return HttpResponse(status=200)
            
        return JsonResponse({'message':'INVALID_KEY'}, status=400)


class CarTypeView(View):
    def post(self, request, model_id):
        data = json.loads(request.body)
        if "type_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.type = CarTypes.objects.get(id=data['type_id'])
            order.save()
            return HttpResponse(status=200)
            
        return JsonResponse({'message':'INVALID_KEY'}, status=400)


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

            return JsonResponse({'data':seat_list}, status=200)

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

            return JsonResponse({'data':wheel_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if "wheel_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.wheel = CarWheels.objects.get(id=data['wheel_id'])
            order.save()
            return HttpResponse(status=200)
            
        return JsonResponse({'message':'INVALID_KEY'}, status=400)


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

            return JsonResponse({'data':interior_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if "interior_id" in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.interior = CarInteriors.objects.get(id=data['interior_id'])
            order.save()
            return HttpResponse(status=200)
            
        return JsonResponse({'message':'INVALID_KEY'}, status=400)


class SpecificationView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('cartypeprices_set').get(id=model_id)
            spec_list = [
            {
                'model_name'       : car.model.model_name,
                'model_type'       : car.type.model_type,
                'acceleration'     : car.acceleration,
                'fuel_economy'     : car.fuel_economy,
                'max_speed'        : car.max_speed,
                'wheel'            : car.wheel,
                'included_options' : car.included_options
            } for car in list(cars.cartypeprices_set.all())]

            return JsonResponse({'data':spec_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

class CarPaymentOptionView(View):

    def get(self, request, model_id):
        try:
            order = CarOrderPrices.objects.get(id=model_id)

            if order.payment.option != 'cash':
                prices = {
                    'monthly_cost' : round(order.expected_price/order.payment.month, 0),
                    'saving_cost'  : round(order.saving_price/order.payment.month, 0)
                }
                return JsonResponse({'data':prices}, status=200)

            return JsonResponse({'message':'NOT_SUPPORTED_FOR_CASH'}, status = 400)
        
        except ZeroDivisionError:
            return JsonResponse({'message':'SELECT_PAYMENTOPTION_FIRST'}, status = 400)

    def post(self, request, model_id):
        data = json.loads(request.body)

        if 'option' in data and 'month' in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.payment = CarPaymentOptions.objects.filter(option=data['option']).get(month=data['month'])
            order.save()
            return HttpResponse(status=200)
            
        return JsonResponse({'message':'INVALID_KEY'}, status=400)

class CarAutoPilotView(View):
    AUTO_SELECTED = 2
    AUTO_NOT_SELECTED = 1

    def post(self, request, model_id):
        data = json.loads(request.body)

        if 'autopilot' in data:
            order = CarOrderPrices.objects.get(id=model_id)
            order.autopilot_price = CarAutoPilots.objects.get(id = self.AUTO_SELECTED if data['autopilot'] == 'True' else self.AUTO_NOT_SELECTED)
            order.save()
            return HttpResponse(status=200)
        
        return JsonResponse({'message':'INVALID_KEY'}, status=400)
