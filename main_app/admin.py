from django.contrib import admin
from .models import Jewelry, Category, Cart

admin.site.register(Category)
admin.site.register(Jewelry)
admin.site.register(Cart)