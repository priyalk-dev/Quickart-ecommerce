from .models import Category

# def menu_categories(request):
#     categories = Category.objects.all()
#     return {'menu_categories': categories}


def menu_categories(request):
    return {'menu_categories': Category.objects.all()}