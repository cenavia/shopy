from django.contrib import admin
from .models import Product

#Registrando el modelo en el admin
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	#definiendo los campos a mostrar en el admin
	list_display =('name','category','descripcion','price',)
	#definiendo categorias a mostrar en el admin
	list_filter =('category',)