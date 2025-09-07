# cartss/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name='cart_home'),  # 🔁 'home' is just a sample view
]
