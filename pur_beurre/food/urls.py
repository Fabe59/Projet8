from django.urls import path, include
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
]