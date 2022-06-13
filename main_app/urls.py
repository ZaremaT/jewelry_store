from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('a/<int:jewelry_id>/', views.JewelryView.as_view(), name="jewelry"),
  path('cart/', views.CartView.as_view(), name="cart"),
  re_path(r'^signup/$', views.signup, name='signup'),
  path('<slug:category>/', views.Home.as_view(), name="home"),
]