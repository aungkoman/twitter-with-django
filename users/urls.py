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
    # path("",views.index,name="index"),
    path("login/", views.sample_login_route, name="sample_login_route"),
    path("login-data/", views.sample_login_route_data, name="sample_login_route_data"),
    #path("user-panel/", views.user_panel, name="user_panel"),
    path("user-panel/", views.profile, name="user_panel"),
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
    path("newsfeed/", views.news_feed, name="news_feed"),
    path("create-article/", views.create_article, name="create_article"),
    path("store-article/", views.store_article, name="store_article"),
    path('article-detail/<int:article_id>/', views.article_detail, name='article_detail'),
    # path('article-detail/<int:article_id>/', views.newsfeed, name='article_detail'),
    path('edit-article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('edit-article-data/<int:article_id>/', views.edit_article_data, name='edit_article_data'),
    path('delete-article/<int:article_id>/', views.delete_article, name='delete_article'),
    path("create-comment/", views.create_comment, name="create_comment"),


    path("profile/", views.profile, name="profile"),
    path("feed/", views.newsfeed, name="feed"),
    path("base/", views.base_layout, name="base_layout"),
    path("login-html/", views.login_html, name="login_html"),
    path("register-html/", views.register_html, name="register_html"),
    path("create-profile-html/", views.create_profile_html, name="create_profile_html"),
    path("", views.test_html, name="test_html"),

    # check login credential, POST
    path("login-check/", views.login_check, name="login_check"),
    path("register-check/", views.register_check, name="register_check"),
    path("store-profile/", views.store_profile, name="store_profile"),
    
]