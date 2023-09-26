from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class UserProfileInfo(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(blank=True,null=True) # If no date is selected then Django saves blank field value.  
    city = models.CharField(max_length=25,blank=True,null=True)
    # file will be uploaded to MEDIA_ROOT/uploads
    profile_picture = models.FileField(upload_to='profile_pictures/', blank=True, null=True)

    # methods
    def __str__(self):
        return self.user.username + " " + self.city

class Article(models.Model):  
    user_profile_info = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    description = models.TextField()
    media = models.FileField(upload_to='article_pictures/', blank=True, null=True)

    # methods
    def __str__(self):
        return self.description

class Comment(models.Model):  
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_profile_info = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    description = models.TextField()
    media = models.FileField(upload_to='comment_pictures/', blank=True, null=True)

    # methods
    def __str__(self):
        return self.description
