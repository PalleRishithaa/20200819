from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from mycontacts import views
urlpatterns=[
        
        url(r'phone.*',views.phone,name='phone'),
        url(r'email.*',views.email,name='email'),
        url(r'',views.nothing,name='nothing'),
        ]
