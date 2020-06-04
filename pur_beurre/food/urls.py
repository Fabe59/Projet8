from django.urls import path
from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

app_name = 'food'
urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('product/<int:id>', views.show, name="show"),
    path('save/', views.save, name="save"),
    path('legals/', views.legals, name="legals"),
    path('sentry-debug/', trigger_error),
]
