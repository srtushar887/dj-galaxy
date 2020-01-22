from django.db import models

# Create your models here.

from category.models import Subcategory
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class generalSetting(models.Model):
    site_title = models.CharField(max_length=100)
    site_email = models.CharField(max_length=50)
    site_logo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    site_icon = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=100,blank=True)
    header_background_color = models.CharField(max_length=100,blank=True)
    footer_background_color = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.site_title


class homeSlider(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    title = models.CharField(max_length=200)
    sort_description = models.TextField(blank=True)
    title_color = models.CharField(max_length=100,blank=True)
    description_color = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title


class CategroyPageContent(models.Model):
    sub_category = models.ForeignKey(Subcategory,on_delete=models.DO_NOTHING)
    page_image = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True)


    def __str__(self):
        return self.sub_category.name


class icon(models.Model):
    icon_name = models.CharField(max_length=100,blank=True)
    icon_link = models.CharField(max_length=100,blank=True)
    icon_code = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.icon_name



