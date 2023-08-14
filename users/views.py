from django.shortcuts import render
# step 1.1 import HttpResponse 
from django.http import HttpResponse
from .forms import UserRegistrationForm, TodoForm

# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    return HttpResponse("Hello World")

def login(request):
    return render(request, 'login.html')

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