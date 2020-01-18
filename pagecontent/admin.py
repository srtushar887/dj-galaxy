from django.contrib import admin

# Register your models here.
from .models import generalSetting,homeSlider,CategroyPageContent

admin.site.register(generalSetting)
admin.site.register(homeSlider)
admin.site.register(CategroyPageContent)