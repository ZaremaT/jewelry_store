from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name="home.html"


class Jewelry(TemplateView):
    template_name="jewelry.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jewelry"] = Jewelry.objects.all() # this is where we add the key into our context object for the view to use
        return context