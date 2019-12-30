from django.urls import path
from .views      import PriceView

urlpatterns = [
    path('/model/<int:model_id>', PriceView.as_view()),
]
