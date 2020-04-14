from django.shortcuts import render

def create(request):
    return render(request, 'users/create.html')

def signin(request):
    return render(request, 'users/signin.html')

