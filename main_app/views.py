from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Jewelry, Cart
import logging


class Home(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jewelrys"] = Jewelry.objects.all()
        return context


class JewelryView(TemplateView):
    template_name="jewelry.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["j"] = Jewelry.objects.get(id=self.kwargs['jewelry_id']) # this is where we add the key into our context object for the view to use
    #     return context
    def get(self, request, *args, **kwargs):
        j = Jewelry.objects.get(id=kwargs['jewelry_id']) # this is where we add the key into our context object for the view to use
        logging.info("get!")
        if request.method == "GET":
            logging.info('GET function: ')
            return render(request, self.template_name, {"j": j})
        
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            logging.info(' not authenticated, added to cart: ' + j.id)
            return render(request, self.template_name, {})
        j = Jewelry.objects.get(id=kwargs['jewelry_id']) # this is where we add the key into our context object for the view to use
        in_cart = Cart.objects.get(username=request.user.username,item_id=j.id)
        if in_cart:
            in_cart.quantity += 1
        else:
            in_cart = Cart(username=request.user.username,item_id=j.id,price=j.price)    
        in_cart.save()
        return render(request, self.template_name, {"j": j})


class CartView(TemplateView):
    template_name="cart.html"
    
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, self.template_name, {"items": items})
        item_ids = Cart.objects.filter(username=request.user.username)
        items = []
        for i in item_ids:
            items.append(Jewelry.objects.get(id=i.item_id))

        return render(request, self.template_name, {"items": items})

