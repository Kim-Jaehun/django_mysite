from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
]
