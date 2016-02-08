from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Enrrutando urls de la app product
    url(r'^', include('product.urls')),
]