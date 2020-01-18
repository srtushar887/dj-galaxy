from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug_name>/<int:category_id>',views.category,name="category"),
]