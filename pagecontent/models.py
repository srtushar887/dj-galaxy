from django.db import models

# Create your models here.
class generalSetting(models.Model):
    site_title = models.CharField(max_length=100)
    site_email = models.CharField(max_length=50)
    site_logo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    site_icon = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)

    def __str__(self):
        return self.site_title


class homeSlider(models.Model):
    image =  models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    title = models.CharField(max_length=200)
    sort_description = models.TextField(blank=True)

    def __str__(self):
        return self.title