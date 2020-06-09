from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
# from django.contrib.admin.widgets import AdminDateWidget
# from django.forms.fields import DateField

# in UserForm we have included the attribute which are present in the User like username,lastname etc
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.CharField()
    lastname = forms.CharField()


    class Meta():
        model = User
        fields = ('username','email','password','firstname','lastname')

# in UserProfileInfoForm we have included the attribute which are present in the UserProfileInfo...
# like portfolio_site,profile_pic
class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','porfile_pic')
