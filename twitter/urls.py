from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # this is new line to add
    path("", include("users.urls")),
    path("admin/", admin.site.urls)
]