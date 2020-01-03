from django.urls import path
from .views      import PriceView, ColorPriceView, WheelPriceView, InteriorPriceView, SpecificationView
from .views      import CarSeatPrice
from .views      import CarPaymentOptionView
from .views      import CarAutoPilotView
from .views      import CarTypeView
from .views      import TotalPriceView


urlpatterns = [
    path('/model/<int:model_id>', PriceView.as_view()),
    path('/option/<int:model_id>', TotalPriceView.as_view()),

    path('/engine/<int:model_id>', CarTypeView.as_view()), # type select

    path('/color/<int:model_id>', ColorPriceView.as_view()),
    path('/wheel/<int:model_id>', WheelPriceView.as_view()),

    path('/interior/<int:model_id>', InteriorPriceView.as_view()),
    path('/specification/<int:model_id>', SpecificationView.as_view()),
    path('/seat/<int:model_id>', CarSeatPrice.as_view()),
    path('/payment/option/<int:model_id>', CarPaymentOptionView.as_view()),
    path('/payment/estimation/<int:model_id>', CarPaymentOptionView.as_view()),   
    path('/autopilot/<int:model_id>', CarAutoPilotView.as_view()),
]
