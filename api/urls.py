from django.urls import path
from .views import CategoryView, CategoryViewDetail, MenuItemView, MenuItemViewDetail, CartView, OrderView, SingleOrderView, UserSerializer
from . import views


urlpatterns = [
    path('categories', CategoryView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryViewDetail.as_view(), name='category-detail'),
    path('menu-items', MenuItemView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>', MenuItemViewDetail.as_view(), name='menu-item-detail'),
    path('cart/menu-items', CartView.as_view(), name='cart-list'),
    path('orders', OrderView.as_view(), name='order-list'),
    path('orders/<int:pk>', SingleOrderView.as_view()),
    path('groups/manager/users', views.GroupViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}))
]

