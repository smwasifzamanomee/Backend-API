from django.urls import path
from .views import LittleLemonView

urlpatterns = [
    path('v1/lemon', LittleLemonView.as_view(), name='lemon'),
]