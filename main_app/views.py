from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Jewelry, Cart
import logging


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jewelrys'] = Jewelry.objects.all()
        return context


class JewelryView(TemplateView):
    template_name = "jewelry.html"

    def get(self, request, *args, **kwargs):
        # this is where we add the key into our context object for the view to use
        j = Jewelry.objects.get(id=kwargs['jewelry_id'])
        if request.method == "GET":
            return render(request, self.template_name, {'j': j})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            logging.info(' not authenticated, added to cart: ' + j.id)
            return render(request, self.template_name, {})
        j = Jewelry.objects.get(id=kwargs['jewelry_id'])
        in_cart, created = Cart.objects.get_or_create(
            username=request.user.username, item_id=j.id, defaults={'price': j.price, 'quantity': 0})
        in_cart.quantity += 1
        in_cart.save()
        return render(request, self.template_name, {"j": j})


class CartView(TemplateView):
    template_name = "cart.html"

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, self.template_name, {})
        item_ids = Cart.objects.filter(username=request.user.username)
        items = []
        for i in item_ids:
            items.append(
                {'quantity': i.quantity, 'item': Jewelry.objects.get(id=i.item_id)})

        return render(request, self.template_name, {'items': items})
