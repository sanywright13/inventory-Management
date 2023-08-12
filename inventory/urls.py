from django.contrib import admin
from django.urls import path,include
from .views import Index , SignUpView ,DashboardView
from django.contrib.auth import views as auth_views
app_name='inventory'
urlpatterns = [
   
    path('',Index.as_view(),name="index"),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('signup/',SignUpView.as_view(),name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name='inventory/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='inventory/logout.html'),name='logout')
    
]
