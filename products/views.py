from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Products,Category,Wishlist,Cart
from django.contrib.auth.decorators import login_required



# Create your views here.



# def products_home(request):
#     products = Products.objects.all()
#     return render(request, {'products': products})

# def category_products(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     products = Products.objects.filter(category=category)
#     return render(request, 'category_products.html', {'category': category, 'products': products})


def product_view(request,id):
    product = get_object_or_404(Products,id=id)
    return render(request,'product_detail.html',{'product':product})
@login_required
def wishlist_view(request):
          wishlist_items = Wishlist.objects.filter(user=request.user)
          return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})
      

@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)

    if wishlist_item.exists():
        wishlist_item.delete()   
    else:
        Wishlist.objects.create(user=request.user, product=product)  

    return redirect(request.META.get('HTTP_REFERER', 'wishlist'))
  
      
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def toggle_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=product)

    if cart_item.exists():
        cart_item.delete()   
    else:
        Cart.objects.create(user=request.user, product=product, quantity=1)  

    return redirect(request.META.get('HTTP_REFERER', 'cart'))

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Products.objects.filter(category=category)

    # collect wishlist + cart product ids for the logged in user
    wishlist_ids = []
    cart_ids = []
    if request.user.is_authenticated:
        wishlist_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
        cart_ids = Cart.objects.filter(user=request.user).values_list('product_id', flat=True)

    return render(request, 'category_products.html', {
        'category': category,
        'products': products,
        'wishlist_ids': wishlist_ids,
        'cart_ids': cart_ids,
    })
