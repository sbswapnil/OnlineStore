from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['pass']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.warning(request, "invalid username or passwword")
                return redirect('login')
        else:
            return render(request, "accounts/login.html")


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['pass']
        c_password = request.POST['cpass']
        email = request.POST['email']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, "Username already Exist !!!")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "Email already Exist !!!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=firstname, last_name=lastname)
                user.save()
                return redirect('login')
        else:
            messages.warning(request, "Password did not match !!!")
            return redirect('signup')

    else:
        return render(request, "accounts/signup.html")


def forgotpass(request):
    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('/')
