from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from events import urls

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error( request, 'Username already exists! Please try some other username')
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signup')                

        if len(username) > 10:
            messages.error(
            request, 'Sorry username must less than 10 characters')
            return redirect('signup')

        if pass1 != pass2:
            messages.warning(request, "Passwords didn't match!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, 'Username must be alphanumeric')
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

        messages.success(request, 'Welcome to Dundaing')

        return redirect('login_view')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        print(request.POST)  # Debugging statement
        username = request.POST.get('username')
        print(f"username: {username}")  # Debugging statement
        password = request.POST.get('pass1')
        print(f"password: {password}")  # Debugging statement
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('index')