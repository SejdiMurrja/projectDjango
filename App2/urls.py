from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage, name='home_page'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact_page'),
]
