from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('xyz',views.index,name='index'),
    path('',views.home,name='home'),
    path('abc',views.show,name='show'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updaterecords/<int:id>',views.updaterecords,name='updaterecords'),
    
]   