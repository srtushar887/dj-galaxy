from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,blank=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    main_category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200,blank=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name
