from django.urls import path
from . import views

urlpatterns = [
    path('v1/test', views.apiTest, name='apiTest'),
    path('v1/testapi', views.testapiView.as_view(), name='testapiView'),
    path('v1/testapi/<int:pk>', views.testapi.as_view(), name='testapi'),
]