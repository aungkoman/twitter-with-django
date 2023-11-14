from django.shortcuts import render, redirect
# step 1.1 import HttpResponse 
from django.http import HttpResponse

from users.models import Article, UserProfileInfo, Comment
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    return render(request, 'index.html')
    # return HttpResponse("Hello World")

def show_login_html(request):
    return render(request, "ui/auth/login.html")

def check_login(request):
    name = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(username = name, password = pwd)
    if user is not None:
        return redirect("user_panel")
    else:
        return redirect("show_login_html")

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
        "user_profile" : user_profile,
        "user" : user
    }
    return render(request, 'user_panel.html', context)


def user_logout(request):
    logout(request)
    # return redirect('test_html')
    return redirect("feed")


def update_user_profile(request):
    user = request.user 
    user_profile =  UserProfileInfo.objects.get(user=user)
    context = {
        "user_profile" : user_profile
    }
    return render(request, 'user_profile/edit.html', context)


def create_user_profile(request):
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
    city = request.POST.get('city')
    dob = request.POST.get('dob')
    profile_picture = request.FILES.get('profile_picture')
    user = request.user
    UserProfileInfo.objects.create(user=user, city=city, dob = dob, profile_picture = profile_picture)
    return redirect('user_panel')


def article_list(request):
    user = request.user 
    user_profile =  None # UserProfileInfo.objects.get(user=user) 
    articles = []
    try:
        user_profile = UserProfileInfo.objects.get(user=user) 
        # tasks = Task.objects.filter(category__name=category_name)
        articles = Article.objects.filter(user_profile_info = user_profile)
    except ObjectDoesNotExist:
        user_profile = None
    context = {
        "user_profile" : user_profile,
        "articles" : articles,
    }
    return render(request, 'articles/article_list.html', context)


def news_feed(request):
    articles = []
    try:
        articles = Article.objects.all()
    except ObjectDoesNotExist:
        user_profile = None
    context = {
        "articles" : articles,
    }
    return render(request, 'newfeed/newfeed.html', context)




def store_article(request):
    user = request.user 
    user_profile =  None # UserProfileInfo.objects.get(user=user) 
    if request.method == 'POST':
        try:
            user_profile = UserProfileInfo.objects.get(user=user) 
            description = request.POST.get("description")
            media = request.FILES.get('media')
            Article.objects.create(user_profile_info=user_profile, description= description, media = media )
        except ObjectDoesNotExist:
            user_profile = None
    # need to add status message
    return redirect("feed")

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article = article)
    context = {
        "article" : article,
        "comments" : comments,
    }
    # return render(request, 'articles/detail.html', context)
    return redirect("feed")

def create_comment(request):
    user = request.user 
    user_profile =  None # UserProfileInfo.objects.get(user=user) 
    if request.method == 'POST':
        try:
        
            article_id = request.POST.get("article_id")
            article = Article.objects.get(id=article_id) 
            user_profile = UserProfileInfo.objects.get(user=user) 
            description = request.POST.get("description")
            # return HttpResponse(article_id)
            media = request.FILES.get('media')
            Comment.objects.create(user_profile_info=user_profile, description= description, media = media, article = article )
        except ObjectDoesNotExist:
            user_profile = None
    # need to add status message
    return redirect('article_detail',article.id)

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        "article" : article
    }
    return render(request, 'articles/edit.html', context)

def edit_article_data(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    description = request.POST.get("description")
    media = request.FILES.get('media')
    article.description = description
    article.media = media
    article.save()
    return redirect('article_detail',article.id)

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("article_list")


"""
try:
    user_profile = UserProfileInfo.objects.get(user=user) 
except ObjectDoesNotExist:
    user_profile = None

def obj_list(request):
    obj_list  = []
    try:
        currentUser = request.user
        obj_list =  Task.objects.filter(user = currentUser)
        return render(request,"ListPage.html",{"myTasks": obj_list})
"""
# own profile since we're tide with request.user
def profile(request):
    user = request.user 
    user_profile =  None # UserProfileInfo.objects.get(user=user) 
    articles = []
    list_for_random = range(100)
    try:
        user_profile = UserProfileInfo.objects.get(user=user) 
    except ObjectDoesNotExist:
        user_profile = None
    
    if user_profile != None :
        try:
            articles = Article.objects.filter(user_profile_info = user_profile).order_by('-id')
        except Exception:
            articles  = []
    
    context = {
        "user_profile" : user_profile,
        "user" : user,
        "articles" : articles,
        "list_for_random" : list_for_random
    }
    # return render(request, 'user_panel.html', context)
    return render(request, 'ui/newsfeed/profile.html', context)

def newsfeed(request):
    # need to pass list of articles
    articles = []
    list_for_random = range(100)
    try:
        articles = Article.objects.all().order_by('-id')
    except ObjectDoesNotExist:
        user_profile = None
    context = {
        "articles" : articles,
        "list_for_random" : list_for_random
    }
    return render(request, 'ui/newsfeed/newsfeed.html', context)

def base_layout(request):
    return render(request, 'ui/layout/base_layout.html')

def login_html(request):
    return render(request, 'ui/auth/login.html')

def register_html(request):
    return render(request, 'ui/auth/register.html')

def test_html(request):
    # return render(request, 'ui/test/test_page.html')
    return redirect("feed")

def create_profile_html(request):
    return render(request, 'ui/auth/create_profile.html')

def login_check(request):
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
        messages.error(request, 'Invalid credentials. Please try again.')
        messages.add_message(request, messages.ERROR, 'Username is required.', 'username_error')
        messages.add_message(request, messages.ERROR, 'Password is required.', 'password_error')
        return redirect('login_html')
        # return HttpResponse("credential does not match " + username + ", " + password) #render(request, 'user_management/login.html')
        # return render(request, 'ui/auth/login.html')

def register_check(request):
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


def store_profile(request):
    if request.user.is_anonymous:
        print("need to login")
        messages.error(request, 'You need to login to create profile')
        return redirect("create_profile_html")
    
    # getting input data from request
    about = request.POST.get('about')
    city = request.POST.get('city')
    dob = request.POST.get('dob')
    profile_picture = request.FILES.get('profile_picture')
    cover_picture = request.FILES.get('cover_picture')

    # return HttpResponse(about)

    
    # check if there is already have one
    # get current logged in user
    user = request.user
    print(user)
    try:
        user_profile = UserProfileInfo.objects.get(user=user) 
        print(user_profile)
        if user_profile != None :
            print("tyring to delete")
            user_profile.delete()
    except ObjectDoesNotExist:
        print("something went wrong")
        # need to redirect back with error message
        # messages.error(request, 'You need to login to create profile')
        # return redirect("test_html")
    
    # store in db
    UserProfileInfo.objects.create(user=user,about=about, city=city, dob = dob, profile_picture = profile_picture, cover_picture= cover_picture)
    # redirect to user_panel
    return redirect('user_panel')


def create_article(request):
    # return render(request, 'articles/create.html')
    return render(request, 'ui/articles/create_article.html')