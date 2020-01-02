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
            # type_list = list(cars.car_models.all().values('type_id','basic_price'))

            type_list = [
            {
                'model_name' : cars.model_name ,
                'basic_price' : car['basic_price'],
                'model_type' : CarTypes.objects.get(id=car['type_id']).model_type,
                'fuel_economy' : car['fuel_economy'],
                'max_speed' : car['max_speed'],
                'acceleration' : car['acceleration'],
                'img_url' : car['img_url']
            } for car in list(cars.car_models.all().values())]

            return JsonResponse({'message':'SUCCESS','data':type_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        print("post start")
        total_price = 0
        data = json.loads(request.body)

        print( [(k, data[k]) for k in data] ) 

        if not 'model_type' in data:
            return JsonResponse({'message':'NO_MODELTYPE'}, status = 400)            

        cars = CarModels.objects.prefetch_related('car_models').get(id=model_id)
        basic_price = list(cars.car_models.filter(type=data['model_type']).values('basic_price'))[0]['basic_price']
        total_price += basic_price


        print("basic price=")
        print(basic_price)
        # if "color_id" in data:
        #     color_price = cars.carcolorprices_set.filter(color_id= data['color_id'])
        #     print( list(color_price.values('color_price'))[0]['color_price'] )
        
        order = CarOrderPrices.objects.get(id=model_id)

        print("order=")
        print(order)
        print(order.color.id)

        car_color = CarColors.objects.prefetch_related('carcolorprices_set').get(id=order.color.id)
        color_price = list( car_color.carcolorprices_set.filter(model=model_id).values('color_price'))[0]['color_price']
        print("color_price=")
        print(color_price)
        total_price += color_price

        #wheel price
        print("wheel=")
        print(order)
        print(order.wheel.id)

        # try carch 필요 IndexError: list index out of range
        car_wheel = CarWheels.objects.prefetch_related('carwheelprices_set').get(id=order.wheel.id)
        wheel_price = list( car_wheel.carwheelprices_set.filter(model=model_id).values('wheel_price'))[0]['wheel_price']
        print("wheel price=")
        print(wheel_price)
        total_price += wheel_price

        print("total price =")
        print(total_price)

        order.expected_price = total_price
        order.saving_price = total_price - PriceView.SAVING_COST
        order.save()

        prices = {
            'expected_price' : order.expected_price,
            'saving_price' : order.saving_price,
        }

        return JsonResponse({'message':'SUCCESS', 'price':prices}, status=200)

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

    def post(self, request, model_id):
        print("color post start")
        data = json.loads(request.body)

        if "color_id" in data:
            print("there is color id")
            # 1. save color_id to CarOrderPrices
            order = CarOrderPrices.objects.get(id=model_id)
            color_type = CarColors.objects.get(id=data['color_id'])
            order.color = color_type
            order.save()
        else:
            print("there is no color id")
            return JsonResponse({'message':'INVALID_KEY'}, status=400)


        return JsonResponse({'message':'SUCCESS'}, status=200)

class WheelPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carwheelprices_set').get(id=model_id)
            wheel_list = list(cars.carwheelprices_set.all().values('wheel_id','wheel_price'))

            for i in range(0, len(wheel_list)):
                car_wheel = CarWheels.objects.get(id=wheel_list[i]['wheel_id'])
                wheel_list[i]['wheel_name'] = car_wheel.wheel_name
                wheel_list[i]['img_url'] = car_wheel.img_url
                del wheel_list[i]['wheel_id']

            return JsonResponse({'message':'SUCCESS','data':wheel_list}, status=200)

        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

    def post(self, request, model_id):
        print("wheel post start")
        data = json.loads(request.body)

        if "wheel_id" in data:
            print("there is wheel id")
            # 1. save color_id to CarOrderPrices
            order = CarOrderPrices.objects.get(id=model_id)
            wheel = CarWheels.objects.get(id=data['wheel_id'])
            order.wheel = wheel
            order.save()
        else:
            print("there is no wheel id")
            return JsonResponse({'message':'INVALID_KEY'}, status=400)


        return JsonResponse({'message':'SUCCESS'}, status=200)


class InteriorPriceView(View):

    def get(self, request, model_id):
        try:
            cars = CarModels.objects.prefetch_related('carinteriorprices_set').get(id=model_id)
            interior_list = list(cars.carinteriorprices_set.all().values('interior_id', 'interior_price', 'descriptions'))

            for i in range(0, len(interior_list)):
                car_interior = CarInteriors.objects.get(id=interior_list[i]['interior_id'])
                interior_list[i]['interior_en_name'] = car_interior.interior_en_name
                interior_list[i]['interior_ko_name'] = car_interior.interior_ko_name
                interior_list[i]['img_url'] = car_interior.img_url
                del interior_list[i]['interior_id']

            return JsonResponse({'message':'SUCCESS','data':interior_list}, status=200)
        
        except CarModels.DoesNotExist:
            return JsonResponse({'message':'INVALID_MODEL'}, status = 400)

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
                'seat_name' : CarSeats.objects.get(id=car['seat_id']).seat_name,
                'seat_price' : car['seat_price']
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
                    'monthly_cost' : order.expected_price/0,
                    # 'monthly_cost' : round(order.expected_price/order.payment.month, 2),
                    'saving_cost' : round(order.saving_price/order.payment.month,2 )
                }
                return JsonResponse({'message':'SUCCESS', 'data':prices}, status=200)
            else:
                return JsonResponse({'message':'NOT_SUPPORTED_FOR_CASH'}, status = 400)
        
        except DivisionByZero:
            return JsonResponse({'message':'PAYMENTOPTION_FIRST'}, status = 400)

    def post(self, request, model_id):
        print("CarPaymentOptionView post start")
        data = json.loads(request.body)

        if 'option' in data and 'month' in data:
            print("there is color id")
            # 1. save payment option to CarOrderPrices
            order = CarOrderPrices.objects.get(id=model_id)
            payment = CarPaymentOptions.objects.filter(option=data['option']).get(month=data['month'])
            order.payment = payment
            order.save()
        else:
            print("there is no color id")
            return JsonResponse({'message':'INVALID_KEY'}, status=400)


        return JsonResponse({'message':'SUCCESS'}, status=200)

class CarAutoPilotView(View):

    def post(self, request, model_id):

        print("CarPaymentOptionView post start")
        data = json.loads(request.body)

        if 'autopilot' in data:
            # 1. save payment option to CarOrderPrices

            print("auto data=")
            print(type( data['autopilot']) )

            order = CarOrderPrices.objects.get(id=model_id)

            # if data['autopilot'] == 'True':
            #     condition = 2
            # else:
            #     condition = 1

            # print("auto_id=")
            # print(condition)

            autopilot = CarAutoPilots.objects.get(id = 2 if data['autopilot'] == 'True' else 1)
            order.autopilot_price = autopilot
            order.save()
        else:
            print("there is no color id")
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)
