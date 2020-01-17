from django.contrib import admin

# Register your models here.
from .models import Category, Subcategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_publish')
    list_display_links = ('id','name')
    list_filter = ('name',)
    list_editable = ('is_publish',)
    search_fields = ('name',)
    list_per_page = 25



class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id','main_category', 'name', 'is_publish')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_publish',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)