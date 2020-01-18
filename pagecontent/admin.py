from django.contrib import admin

# Register your models here.
from .models import generalSetting,homeSlider

admin.site.register(generalSetting)
admin.site.register(homeSlider)