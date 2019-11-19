from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from register.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def Register(request):
    """ function for user registration
    """
    if request.method == "POST":      
        form = UserRegisterForm(request.POST )
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}!, votre compte a ete cree')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register/user.html', {'form': form})


@login_required(login_url = 'login')
def compte(request):
    """ Display Details of User
    """
    return render(request, 'store/compte.html', locals())