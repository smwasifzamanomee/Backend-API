from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.index, name='index'),
    path('api/date/', views.display_date, name='display_date'),
    path('api/user/', views.getUser, name='getUser'),
    path('api/path/<str:name>/<int:id>/', views.pathview, name='pathview'),
    path('api/query/', views.qryview, name='qryview'),
    path('api/form/', views.showform, name='showform'),
    path('api/book', views.book, name='book')
]
