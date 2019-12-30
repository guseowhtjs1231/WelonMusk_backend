from django.urls import path
from .views      import ColorPriceView

urlpatterns = [
    path('/color/<int:model_id>', ColorPriceView.as_view()),
]
