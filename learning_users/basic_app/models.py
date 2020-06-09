from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# This is a model class to add a additional info that the default User doesnt have.
# Remember that default User already has things like username,password,email,firstname,lastname.
# if u want to add more attribute to the user we can extend the class by using OneToOneField relationships.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional attributes of this model
    # blank - true means that the user doesn't have to fill it our compulsory user can even leave it.
    portfolio_site =models.URLField(blank = True)
    porfile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
