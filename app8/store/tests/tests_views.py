from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve
from store.models import Product, Favorite, Categorie
from register.models import Profile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.resultats_url = reverse('resultats')
        self.aliment_url = reverse('aliment')
        self.home_url = reverse('home')
        self.save_aliment_url = reverse('save_aliment', args=[1, 2, 3])
        self.user = User.objects.create_user('wafi', 'wafi@gmail.com', 'wafipass')
        self.profile = Profile.objects.get_or_create(user=self.user)


    def test_home_get(self):
            response = self.client.get(self.home_url)
            self.assertEquals(response.status_code, 200)

    def test_resultats_get(self):
        self.client.login(username= 'wafi', password='wafipass') 
        response = self.client.get(self.resultats_url, data={'query': 'Coca'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/home.html')

    def test_aliment_get(self):
        self.client.login(username= 'wafi', password='wafipass') 
        response = self.client.get(self.aliment_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/aliment.html')
    
    
    def save_aliment(self):
        self.client.login(username= 'wafi', password='wafipass') 
        response = self.client.get(self.save_aliment_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/save_aliment.html')


    def test_resultats_get_redirect(self):
        response = self.client.get(self.resultats_url)
        self.assertEquals(response.status_code, 302)

    def test_aliment_get_redirect(self):
        response = self.client.get(self.aliment_url)
        self.assertEquals(response.status_code, 302)
    
    
    def save_aliment_redirect(self):
        response = self.client.get(self.save_aliment_url)
        self.assertEquals(response.status_code, 302)