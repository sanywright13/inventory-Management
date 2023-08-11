from django.contrib import admin
from django.urls import path,include
from .views import Index , SignUpView
app_name='inventory'
urlpatterns = [
   
    path('',Index.as_view(),name="index"),
    path('signup/',SignUpView.as_view(),name="signup")
]
