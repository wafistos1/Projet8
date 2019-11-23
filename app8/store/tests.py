from django.test import TestCase
from django.urls import reverse 

# Create your tests here.

"""
! testviews
todo 

? home
? resultats
? aliment
? save_aliment
? detail_favori

"""

class homeTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_resultat_page(self):
        response = self.client.get(reverse('resultats'))
        self.assertEqual(response.status_code, 200)

    def test_aliment_page(self):
        response = self.client.get(reverse('aliment'))
        self.assertEqual(response.status_code, 200)

"""
! testModel
? Product
? Favorite
"""
"""
! testUrl
? home
? resultats
? resultats/<int:page>
? aliment
? aliment/<int:fav>/<int:prod>/<int:user>/
? detail_favori/<int:pk>

"""

