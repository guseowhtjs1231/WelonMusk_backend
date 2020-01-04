from django.urls import path
from .views      import PriceView, ColorPriceView
from .views      import WheelPriceView
from .views      import InteriorPriceView
from .views      import SpecificationView

urlpatterns = [
    path('/model/<int:model_id>', PriceView.as_view()),
    path('/color/<int:model_id>', ColorPriceView.as_view()),
    path('/wheel/<int:model_id>', WheelPriceView.as_view()),
    path('/interior/<int:model_id>', InteriorPriceView.as_view()),
    path('/specification/<int:model_id>', SpecificationView.as_view()),
]
