from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('insert/user/message', views.save_message, name='save_message'),

]