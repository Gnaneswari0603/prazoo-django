from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('design/',views.design,name='design'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
]