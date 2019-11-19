from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from store.models import Product
import requests

class Command(BaseCommand):
    help = 'Uplaod data from OpenFactFood API'

    # def add_arguments(self, parser):
    #     parser.add_arguments('upload', type=str, help='upload data from OpenFactFood API')
    
    def handle(self, *args, **Kwargs):
        # Bit of logic to upload data
        
        """Loads the API data into a Json file and returns it
        """
        api_search = 'https://world.openfoodfacts.org/cgi/search.pl?/get'
        payload = {
            'search_terms': 'soda',
            'json': 1,
            'page_size': 100,
            }
        json_data = requests.get(api_search, params=payload).json()
        taille = len(json_data['products'])
        # print(json_data['products'][0])
        print(taille)
        # The loop that inserts the data into my tables
        for i in range(taille):
            try:
                name = json_data['products'][i]['product_name']
                grade = json_data['products'][i]['nutrition_grades_tags'][0]
                image = json_data['products'][i]['image_url']
                product = Product.objects.get_or_create(name=name, grade=grade, images=image)
            except(KeyError, TypeError):
                continue
            except IntegrityError:
                continue
        
        self.stdout.write(self.style.SUCCESS('upload data done'))