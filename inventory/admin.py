from django.contrib import admin

# Register your models here.
from .models import Category , InventoryItem 
admin.site.register(Category)
admin.site.register(InventoryItem)