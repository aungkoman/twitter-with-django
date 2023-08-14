from django.urls import path
from . import views

urlpatterns = [
    # add first element to urlpatterns array
    # path function accept two parameter
    # first parameter is url path
    # second parameter is function name 
    path("hello/", views.index),
    path("login/", views.login_route, name="login"),
    path("register/", views.register, name="register"),
    path("user-panel/", views.user_panel, name="user_panel"),
    path("update/", views.update, name="update"),
]