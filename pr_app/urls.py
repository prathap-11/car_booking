from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('pricing/',views.pricing,name='pricing'),
    path('car/',views.car,name="car"),
    path('car-single/',views.car_Single,),
    path('blog/',views.blog,name="blog"),
    path('blog-single/',views.blog_Single),
    path('contact/',views.contact,name="contact"),
    path('main/',views.main),
    path('trial/',views.trial)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);