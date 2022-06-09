from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('a/<int:jewelry_id>/', views.Jewelry.as_view(), name="jewelry")
]