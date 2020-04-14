from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('create/', views.create, name="create"),
    path('signin/', views.signin, name="signin")
]