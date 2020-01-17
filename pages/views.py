from django.shortcuts import render

# Create your views here.

from category.models import Category,Subcategory

def index(request):
    maincategory = Category.objects.filter(is_publish=True)
    subcategory = Subcategory.objects.filter(is_publish=True)
    context = {
        'maincategory' : maincategory,
        'subcategory' : subcategory
    }
    return render(request,'pages/index.html',context)