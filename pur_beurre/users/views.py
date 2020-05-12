from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from food.models import Favorites, Product
from django.core.paginator import Paginator

def create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/create.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
    
@login_required
def fav(request):
    user = request.user
    favs = Favorites.objects.filter(user=user)
    favs_id = []
    for fav in favs:
        favs_id.append(fav.substitute_id)
    liste_prod_fav = []
    for id in favs_id:
        liste_prod_fav.append(Product.objects.get(id=id))

    paginator = Paginator(liste_prod_fav, 6)
    page_number = request.GET.get('page')
    page_fav = paginator.get_page(page_number)

    return render(request, 'users/fav.html', {'liste_prod_fav':page_fav})

def delete_fav(request):
    if request.method == "POST":
        user = request.user
        elt = request.POST.get('elt')
        elt = Product.objects.get(id=elt)
        elt_delete = Favorites.objects.filter(user=user, substitute=elt)
        elt_delete.delete()
    return render(request, 'food/home.html')

