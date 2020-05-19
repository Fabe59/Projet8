from django.test import TestCase
from django.urls import reverse, resolve
from food.views import home, search, show, save, legals
from food.models import Category, Product, Favorites
from users.views import create, profile, fav, delete_fav
from users.forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

"""Test de l'app Food"""


class Food_Url_Test(TestCase):

    def test_home_url_resolves(self):
        url = reverse('food:home')
        self.assertEquals(resolve(url).func, home)

    def test_search_url_resolves(self):
        url = reverse('food:search')
        self.assertEquals(resolve(url).func, search)

    def test_show_url_resolves(self):
        url = reverse('food:show', args=['123'])
        self.assertEquals(resolve(url).func, show)

    def test_save_url_resolves(self):
        url = reverse('food:save')
        self.assertEquals(resolve(url).func, save)

    def test_legals_url_resolves(self):
        url = reverse('food:legals')
        self.assertEquals(resolve(url).func, legals)


class ModelsTest(TestCase):

    def test_cat_insertion(self):
        cat = Category.objects.create(name='bonbons')
        self.assertEqual(Category.objects.first(), cat)

    def test_cat_string_representation(self):
        cat = Category.objects.create(name='bonbons')
        self.assertEqual(str(cat), 'bonbons')

    def test_prod_insertion(self):
        prod = Product.objects.create(brand='LU', name='BN')
        self.assertEqual(Product.objects.first(), prod)

    def test_prod_string_representation(self):
        prod = Product.objects.create(brand='LU', name='BN')
        self.assertEqual(str(prod), 'LU, BN')


class HomepageViews(TestCase):

    def test_homepage(self):
        response = self.client.get(reverse('food:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')


class LegalsViews(TestCase):

    def test_legals(self):
        response = self.client.get(reverse('food:legals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/legals.html')


class SearchViews(TestCase):

    def setUp(self):
        nutella = {
            'id': '312',
            'brand': 'Ferrero',
            'name': 'Nutella',
            'nutrition_grade_fr': "e",
            'image_nutrition_url': 'https://nutnut.jpg',
            'image_url': 'https://nut.jpg',
        }
        nutella = Product.objects.create(**nutella)
        self.nutella = nutella

    def test_foodsearch_valid(self):
        response = self.client.get('/search/?search=%s' % ('nutella'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/nosubstitute.html')

    def test_foodsearch_empty(self):
        response = self.client.get('/search/?search=%s' % (''))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/home.html')


class ShowViews(TestCase):

    def setUp(self):
        nutella = {
            'id': '312',
            'brand': 'Ferrero',
            'name': 'Nutella',
            'nutrition_grade_fr': "e",
            'image_nutrition_url': 'https://nutnut.jpg',
            'image_url': 'https://nut.jpg',
        }
        nutella = Product.objects.create(**nutella)
        self.nutella = nutella

    def test_foodshow_valid(self):
        id = self.nutella.id
        response = self.client.get('/product/%d' % (id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food/show.html')


class SaveViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                 self.username,
                 self.email,
                 self.password
                 )

        nutella = {
            'id': '312',
            'brand': 'Ferrero',
            'name': 'Nutella',
            'nutrition_grade_fr': "e",
            'image_nutrition_url': 'https://nutnut.jpg',
            'image_url': 'https://nut.jpg',
        }
        nutella = Product.objects.create(**nutella)
        self.nutella = nutella

    def test_save_substitute(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('food:save')
        data = {"elt": self.nutella.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Favorites.objects.all().exists())


"""Test de l'app Users"""


class Users_Url_Test(TestCase):

    def test_create_url_resolves(self):
        url = reverse('users:create')
        self.assertEquals(resolve(url).func, create)

    def test_profile_url_resolves(self):
        url = reverse('users:profile')
        self.assertEquals(resolve(url).func, profile)

    def test_fav_url_resolves(self):
        url = reverse('users:fav')
        self.assertEquals(resolve(url).func, fav)

    def test_delete_fav_url_resolves(self):
        url = reverse('users:delete_fav')
        self.assertEquals(resolve(url).func, delete_fav)

    def test_login_url_resolves(self):
        url = reverse('users:login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_resolves(self):
        url = reverse('users:logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)


class Users_Form_TestCase(TestCase):

    def test_user_creation_forms_is_valid(self):
        form = CustomUserCreationForm(data={
            "username": "Paulo",
            "email": "paulo@free.fr",
            "password1": "Purbeurre2020",
            "password2": "Purbeurre2020"
            })
        self.assertTrue(form.is_valid())

    def test_user_creation_forms_is_not_valid(self):
        form = CustomUserCreationForm(data={
            "username": "Paulo",
            "email": "paulo@free.fr",
            "password1": "Purbeurre2020",
            "password2": "Azerty"
        })
        self.assertFalse(form.is_valid())

    def test_user_creation_forms_email_is_not_valid(self):
        form = CustomUserCreationForm(data={
            "username": "Paulo",
            "email": "Paulo.fr",
            "password1": "Purbeurre2020",
            "password2": "Purbeurre2020"
        })
        self.assertFalse(form.is_valid())


class CreateViews(TestCase):

    def test_create_page(self):
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

    def test_create_account_valid(self):
        response = self.client.post(reverse('users:create'), {
            'username': 'usernametest',
            'email': 'emailtest@free.fr',
            'password': 'megamotdepasse'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users:profile')


class LoginViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_login(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


class Logoutviews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')


class ProfileViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

    def test_account_when_logged_in(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_account_when_logged_out(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/users/profile/')


class FavViews(TestCase):

    def setUp(self):
        self.username = 'papa'
        self.email = 'papa@aol.com'
        self.password = 'megamotdepasse'
        self.user = User.objects.create_user(
                self.username,
                self.email,
                self.password
                )

        nutella = {
            'id': '312',
            'brand': 'Ferrero',
            'name': 'Nutella',
            'nutrition_grade_fr': "e",
            'image_nutrition_url': 'https://nutnut.jpg',
            'image_url': 'https://nut.jpg',
        }
        nutella = Product.objects.create(**nutella)
        self.nutella = nutella
        food_saved = Product.objects.get(id=self.nutella.id)
        Favorites.objects.create(user=self.user, substitute=food_saved)

    def test_fav_when_logged_in(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('users:fav'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/fav.html')

    def test_fav_when_logged_out(self):
        response = self.client.get(reverse('users:fav'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/users/fav/')