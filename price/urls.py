from django.urls import path
from .views      import PriceView, ColorPriceView
from .views      import WheelPriceView

urlpatterns = [
    path('/model/<int:model_id>', PriceView.as_view()),
    path('/color/<int:model_id>', ColorPriceView.as_view()),
    path('/wheel/<int:model_id>', WheelPriceView.as_view()),
]
