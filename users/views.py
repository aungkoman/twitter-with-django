from django.shortcuts import render, redirect
# step 1.1 import HttpResponse 
from django.http import HttpResponse

from users.models import UserProfileInfo
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    return render(request, 'index.html')
    # return HttpResponse("Hello World")


def sample_register_route(request):
    return render(request, 'user_management/register.html')

def sample_register_route_data(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect("user_panel")
    else:
        # No backend authenticated the credentials
        return HttpResponse("register failed :  " + username + ", " + password) #render(request, 'user_management/login.html')


def sample_login_route(request):
    return render(request, 'user_management/login.html')

def sample_login_route_data(request):
    # login using username and password
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username= username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        
        return redirect("user_panel")
    else:
        # No backend authenticated the credentials
        return HttpResponse("credential does not match " + username + ", " + password) #render(request, 'user_management/login.html')
    

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
    user = request.user 
    user_profile =  None # UserProfileInfo.objects.get(user=user) 
    try:
        user_profile = UserProfileInfo.objects.get(user=user) 
    except ObjectDoesNotExist:
        user_profile = None
    context = {
        "hello" : "world",
        "user_profile" : user_profile
    }
    return render(request, 'user_panel.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def update_user_profile(request):
    user = request.user 
    user_profile =  UserProfileInfo.objects.get(user=user)
    context = {
        "user_profile" : user_profile
    }
    return render(request, 'user_profile/edit.html', context)


def create_user_profile(request):
    user = request.user 
    return render(request, 'user_profile/create.html')

def update_user_profile_data(request):
    user = request.user 
    user_profile =  UserProfileInfo.objects.get(user=user)
    # update 
    if request.method == 'POST':
        city = request.POST.get('city')
        dob = request.POST.get('dob')
        profile_picture = request.FILES.get('profile_picture')
        user_profile.city = city
        user_profile.dob = dob
        user_profile.profile_picture = profile_picture
        user_profile.save()
        # todo.title = title
        # todo.save()
        return redirect('user_panel')
    return redirect('update_user_profile')


def delete_user_profile_data(request):
    user = request.user 
    try:
        user_profile = UserProfileInfo.objects.get(user=user) 
        user_profile.delete()
        return redirect('user_panel')
    except ObjectDoesNotExist:
        return redirect('user_panel')
    

def create_user_profile_data(request):
    # update 
    if request.method == 'POST':
        user = request.user 
        user_profile =  UserProfileInfo.objects.create()
        city = request.POST.get('city')
        dob = request.POST.get('dob')
        profile_picture = request.FILES.get('profile_picture')
        user_profile.city = city
        user_profile.dob = dob
        user_profile.profile_picture = profile_picture
        user_profile.user = user
        user_profile.save()
        return redirect('user_panel')
    return redirect('user_panel')