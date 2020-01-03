from django.urls import path
from .views      import PriceView, ColorPriceView
from .views      import InteriorPriceView

urlpatterns = [
    path('/model/<int:model_id>', PriceView.as_view()),
    path('/color/<int:model_id>', ColorPriceView.as_view()),
    path('/interior/<int:model_id>', InteriorPriceView.as_view()),
]
