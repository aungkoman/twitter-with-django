from django.shortcuts import render, redirect
# step 1.1 import HttpResponse 
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth import logout

# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    return HttpResponse("Hello World")


def sample_login_route(request):
    return render(request, 'user_management/login.html')

def login_route(request):
    """
    User Registration form

    Args:
        request (POST): New user registered
    """    
    form = UserRegistrationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("user_panel")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, 'login.html', context)

def register(request):
    """
    User Registration form

    Args:
        request (POST): New user registered
    """    
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("login")
            return HttpResponse("User Registred")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    # return render(request, "todo/register.html", context)
    """
        Register.html က ဖောင်ဘယ်လိုပြမလဲ?
        
    """
    return render(request, 'register.html', context)

def update(request):
    return render(request, 'update.html')

def user_panel(request):
    return render(request, 'user_panel.html')


def user_logout(request):
    logout(request)
    return redirect('login')