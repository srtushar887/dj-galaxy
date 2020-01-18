from django.shortcuts import render,redirect

# Create your views here.
from .models import userMessage
from category.models import Category,Subcategory
from pagecontent.models import generalSetting
def contact(request):
    maincategory = Category.objects.filter(is_publish=True)
    subcategory = Subcategory.objects.filter(is_publish=True)
    general_setting = generalSetting.objects.all()[:1].get()
    context = {
        'maincategory': maincategory,
        'subcategory': subcategory,
        'general_setting':general_setting

    }
    return render(request,'contact/contact.html',context)

def save_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = userMessage.objects.create(full_name=name,email=email,subject=subject,message=message)
        contact.save()
