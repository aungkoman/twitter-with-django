from django.urls import path
from . import views

urlpatterns = [
    # add first element to urlpatterns array
    # path function accept two parameter
    # first parameter is url path
    # second parameter is function name 
    path("hello/", views.index),
    # path("login/", views.login_route, name="login"),
    # path("register/", views.register, name="register"),
    path("",views.index,name="index"),
    path("login/", views.sample_login_route, name="sample_login_route"),
    path("login-data/", views.sample_login_route_data, name="sample_login_route_data"),
    path("user-panel/", views.user_panel, name="user_panel"),
    path("logout/", views.user_logout, name="logout"),
    path("update/", views.update, name="update"),
    path("register/", views.sample_register_route, name="sample_register_route"),
    path("register-data/", views.sample_register_route_data, name="sample_register_route_data"),

    path("update-user-profile/", views.update_user_profile, name="update_user_profile"),
    path("update-user-profile-data/", views.update_user_profile_data, name="update_user_profile_data"),
    path("delete-user-profile-data/", views.delete_user_profile_data, name="delete_user_profile_data"),
    path("create-user-profile/", views.create_user_profile, name="create_user_profile"),
    path("create-user-profile-data/", views.create_user_profile_data, name="create_user_profile_data"),

    path("article-list/", views.article_list, name="article_list"),
    path("create-article/", views.create_article, name="create_article"),
    path("create-article-data/", views.create_article_data, name="create_article_data"),
    path('article-detail/<int:article_id>/', views.article_detail, name='article_detail'),
    
]