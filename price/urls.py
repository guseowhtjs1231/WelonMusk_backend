from django.urls import path
from .views      import PriceView, ColorPriceView
from .views      import CarSeatPrice
from .views      import WheelPriceView
from .views      import InteriorPriceView
from .views      import SpecificationView
from .views      import TotalPriceView
from .views      import CarPaymentOptionView
from .views      import CarTypeView

urlpatterns = [
    path('/model/<int:model_id>', PriceView.as_view()),
    path('/engine/<int:model_id>', CarTypeView.as_view()),
    path('/color/<int:model_id>', ColorPriceView.as_view()),
    path('/seat/<int:model_id>', CarSeatPrice.as_view()),
    path('/wheel/<int:model_id>', WheelPriceView.as_view()),
    path('/interior/<int:model_id>', InteriorPriceView.as_view()),
    path('/specification/<int:model_id>', SpecificationView.as_view()),
    path('/option/<int:model_id>', TotalPriceView.as_view()),
    path('/payment/option/<int:model_id>', CarPaymentOptionView.as_view()),
    path('/payment/estimation/<int:model_id>', CarPaymentOptionView.as_view()),
]
