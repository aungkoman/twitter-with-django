from django.contrib import admin

# Register your models here.
from .models import UserProfileInfo, Article

admin.site.site_header = "Twitter"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Twitter"

admin.site.register(UserProfileInfo)
admin.site.register(Article)