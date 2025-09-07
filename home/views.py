from django.shortcuts import render
from django.db.models import Q
from products.models import Products

# Create your views here.

def home(request):
    return render(request,'home.html')


def products_list(request):
    query = request.GET.get('q')
    if query:
        products = Products.objects.filter(
          Q(name__icontains=query) | Q(description__icontains=query)
    ).distinct()
        
        suggestions = Products.objects.filter(
        name__icontains =query
        ).values_list('name',flat=True)[:5]
        
    else:
        products = None
        suggestions= None 
    return render(request, 'category_products.html', {
        'products': products,
        'query': query,
        'suggestions': suggestions
    })
        

