from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('a/<int:jewelry_id>/', views.JewelryView.as_view(), name="jewelry"),
  path('cart/<inbt:pk>/', views.CartView.as_view(), name="cart"),
  path('cart/<int:pk>/update',views.CartUpdate.as_view(), name="cart_update"),
  path('cart/<int:pk>/delete',views.CartDelete.as_view(), name="cart_delete"),
]