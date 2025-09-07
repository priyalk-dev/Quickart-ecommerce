from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('products_list/',views.products_list,  name='products_list'),
]
