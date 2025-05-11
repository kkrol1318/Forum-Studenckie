# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.shortcuts import render, redirect
# - rejestracja
from . forms import CreateUserForm, LoginForm
# - logowanie
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def cars(request):
    values = {
        'cars': [
            {
                'car': 'Nissan 350Z',
                'year': 2003,
                'drive_wheel': 'rwd',
                'color': 'orange',
                'price': '$35,000',
            },
            {
                'car': 'Mitsubishi Lancer Evolution VIII',
                'year': 2004,
                'drive_wheel': '4wd',
                'color': 'yellow',
                'price': '$36,000',
            },
            {
                'car': 'Ford Mustang GT (Gen. 5)',
                'year': 2005,
                'drive_wheel': 'rwd',
                'color': 'red',
                'price': '$36,000',
            },
            {
                'car': 'BMW M3 GTR (E46)',
                'year': 2005,
                'drive_wheel': 'rwd',
                'color': 'blue and gray',
                'price': 'Priceless',
            },
        ]
    }

    return render(request, 'main/cars.html', values)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


#NASZE PODSTRONY
from django.shortcuts import render

def kolo1(request):
    return render(request, 'main/kolo-1.html')

def kolo2(request):
    return render(request, 'main/kolo-2.html')

def kolo3(request):
    return render(request, 'main/kolo-3.html')

def kolo4(request):
    return render(request, 'main/kolo-4.html')

#- Rejsetracja
def register(request):

    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect("login")
    context = {'registerform':form}
    return render(request, 'main/register.html', context=context)

# - logowanie

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                
                auth.login(request, user)
                
                return redirect("home")
    
    context = {'loginform':form}
    
    
    return render(request, 'main/login.html', context=context)

def user_logout(request):
    
    auth.logout(request)
    
    return redirect("home")


@login_required(login_url='login')
def new_post(request):
    form = forms.CreatePost()
    return render(request, 'main/new_post.html', { 'form': form})