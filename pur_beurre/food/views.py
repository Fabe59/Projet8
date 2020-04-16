from django.shortcuts import render
from .models import Product, Category

def home(request):
    return render(request, 'food/home.html')

def search(request):
    research = request.GET['search']
    results = Product.objects.filter(name__icontains=research).order_by('nutrition_grade_fr')

    return render(request, 'food/search.html', {'search':results})