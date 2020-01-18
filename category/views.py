from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Category,Subcategory
from pagecontent.models import CategroyPageContent
def category(request,slug_name,category_id):
    maincategory = Category.objects.filter(is_publish=True)
    subcategory = Subcategory.objects.filter(is_publish=True)
    category = get_object_or_404(Subcategory,slug=slug_name)
    pageContent = get_object_or_404(CategroyPageContent,sub_category_id=category_id)
    context = {
        'maincategory': maincategory,
        'subcategory': subcategory,
        'pageContent':pageContent
    }
    return render(request,'category/categoryPage.html',context)