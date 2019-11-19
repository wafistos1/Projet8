from django.shortcuts import render, get_object_or_404
from store.models import Product, Favorite
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Global variable
query = None


def home(request):
    return render(request, 'store/home.html')


@login_required(login_url = 'login')
def resultats(request, page=1):
    """Displays the results of the search for substitute products 
    """
    global query
    if request.GET.get('q') is None:
        pass
    else:
        query = request.GET.get('q')
    print(query)
    try:
        data = Product.objects.filter(name=query)
        data[0]
        best_product = Product.objects.filter(grade__lt=data[0].grade).order_by("grade")
        paginator = Paginator(best_product, 15)
        best_product = paginator.page(page)
    except IndexError:
        print("Pas de produit essayez une autre recherche svp")
    except EmptyPage:
        paginator = paginator.page(paginator.num_pages)
    return render(request, 'store/resultats.html', {'data': data[0], 'best_product': best_product})


@login_required(login_url = 'login')
def aliment(request):
    """Display all aliment favorite of user
    """
    favorite = Favorite.objects.filter(user=request.user).select_related('product_choice', 'product_favorite', 'user')
    return render(request, 'store/aliment.html', {'favorites': favorite})



@login_required(login_url = 'login')
def save_aliment(request, fav, prod, user):
    """saves the food that the user has chosen in the database
    """
    favorite_product = Product.objects.filter(pk=fav)
    choice_product = Product.objects.filter(pk=prod)
    user = User.objects.filter(pk=user)
    print(user[0].pk, favorite_product[0].pk, choice_product[0].pk)
    favorite = Favorite.objects.get_or_create(
        product_choice=choice_product[0],
        product_favorite=favorite_product[0],
         user=user[0]
         )
    return render(request, 'store/save_aliment.html', {'favorite': favorite[0]})
