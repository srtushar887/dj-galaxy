from django.shortcuts import render

# Create your views here.

from category.models import Category,Subcategory
from pagecontent.models import generalSetting,icon

def index(request):
    maincategory = Category.objects.filter(is_publish=True)
    subcategory = Subcategory.objects.filter(is_publish=True)
    general_setting = generalSetting.objects.all()[:1].get()
    icons = icon.objects.all()
    context = {
        'maincategory' : maincategory,
        'subcategory' : subcategory,
        'general_setting':general_setting,
        'icons' :icons
    }
    return render(request,'pages/index.html',context)