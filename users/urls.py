from django.contrib import admin
from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.SigninView.as_view(), name='login'),
    path('logout/', views.SignoutView.as_view(), name='logout'),
]
