from django.contrib import admin

# Register your models here.
from .models import generalSetting,homeSlider,CategroyPageContent,icon

admin.site.register(generalSetting)
admin.site.register(homeSlider)
admin.site.register(CategroyPageContent)
admin.site.register(icon)