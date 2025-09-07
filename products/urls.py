# products/urls.py

from django.urls import path
from . import views
from .models import Wishlist

urlpatterns = [
    # path('products/',views.products_home,name="products_home"),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>',views.product_view,name='product_view'),
    path('wishlist/',views.wishlist_view,name='wishlist'),
    path('cart/',views.cart_view,name="cart"),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('cart/toggle/<int:product_id>/', views.toggle_cart, name='toggle_cart'),
]
