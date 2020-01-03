from django.urls import path
from .views      import PriceView, ColorPriceView
from .views      import CarSeatPrice

urlpatterns = [
    path('/model/<int:model_id>', PriceView.as_view()),
    path('/color/<int:model_id>', ColorPriceView.as_view()),
    path('/seat/<int:model_id>', CarSeatPrice.as_view()),
]
