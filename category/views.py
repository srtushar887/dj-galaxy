from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Category,Subcategory
from pagecontent.models import CategroyPageContent
from pagecontent.models import generalSetting
def category(request,slug_name,category_id):
    maincategory = Category.objects.filter(is_publish=True)
    subcategory = Subcategory.objects.filter(is_publish=True)
    category = get_object_or_404(Subcategory,slug=slug_name)
    pageContent = get_object_or_404(CategroyPageContent,sub_category_id=category_id)
    general_setting = generalSetting.objects.all()[:1].get()
    context = {
        'maincategory': maincategory,
        'subcategory': subcategory,
        'pageContent':pageContent,
        'general_setting': general_setting
    }
    return render(request,'category/categoryPage.html',context)