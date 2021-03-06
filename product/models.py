from __future__ import unicode_literals

from django.db import models

#definimos la campos del modelo
class Product(models.Model):
	name = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__ (self):
		return self.name