from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Jewelry


class Home(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jewelrys"] = Jewelry.objects.all()
        return context


class JewelryView(TemplateView):
    template_name="jewelry.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["j"] = Jewelry.objects.get(id=self.kwargs['jewelry_id']) # this is where we add the key into our context object for the view to use
        return context
