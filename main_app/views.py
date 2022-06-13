from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import  UpdateView, DeleteView
from .models import Jewelry, Cart, Category
import logging
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['jewelrys'] = Jewelry.objects.filter(category=kwargs['category'])
        except:
            context['jewelrys'] = Jewelry.objects.all()
        context['categories'] = Category.objects.all()
        return context
    
    


class JewelryView(TemplateView):
    template_name = "jewelry.html"

    def get(self, request, *args, **kwargs):
        # this is where we add the key into our context object for the view to use
        j = Jewelry.objects.get(id=kwargs['jewelry_id'])
        if request.method == "GET":
            return render(request, self.template_name, {'j': j, 'categories': Category.objects.all()})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            logging.info(' not authenticated, added to cart: ' + j.id)
            return render(request, self.template_name, {})
        j = Jewelry.objects.get(id=kwargs['jewelry_id'])
        in_cart, created = Cart.objects.get_or_create(
            username=request.user.username, item_id=j.id, defaults={'price': j.price, 'quantity': 0})
        in_cart.quantity += 1
        in_cart.save()
        return render(request, self.template_name, {"j": j, 'categories': Category.objects.all()})


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

        return render(request, self.template_name, {'items': items, 'categories': Category.objects.all()})
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name, {})
        item_ids = Cart.objects.filter(username=request.user.username).order_by('item_id')
        items = []
        
        action = ''
        id = -1
        if 'plus-cart' in request.POST:
            action = 'plus-cart'
        elif 'minus-cart' in request.POST:
            action = 'minus-cart'
        else:
            return render(request, self.template_name, {})
        id = request.POST[action]
        for i in item_ids:
            if i.item_id == id:
                if action == 'plus-cart':
                    i.quantity += 1
                elif action == 'minus-cart':  
                    i.quantity -= 1
                
                if i.quantity == 0:
                    Cart.objects.filter(id=i.id).delete()
                else:
                    Cart.objects.filter(id=i.id).update(quantity=i.quantity)
                    items.append({'quantity': i.quantity, 'item': Jewelry.objects.get(id=i.item_id)})
            else:
                items.append({'quantity': i.quantity, 'item': Jewelry.objects.get(id=i.item_id)})
        
        return render(request, self.template_name, {'items': items, 'categories': Category.objects.all()})

    
class CartUpdate(UpdateView):
    model = Cart
    fields = ['id','name', 'img', 'category', 'desciption', 'price']
    template_name = "cart_update.html"
    
class CartDelete(DeleteView):
    model = Cart
    template_name = "cart_delete_confirmation.html"
    success_url = "/cart/"
