from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('a/<int:jewelry_id>/', views.JewelryView.as_view(), name="jewelry"),
  path('cart/', views.CartView.as_view(), name="cart")
]