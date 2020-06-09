from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# For Login Logouts
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are Successfully Logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            #in 1st line we are grabing the userform and saving it in the database->(user)
            # and in 2nd line we are hashing the password the using set password method
            #and then in 3rd line we save the hashed password in the database
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            #we will do the same technique when we will be dealing with the pdf,resume we say request.FILES
            if 'porfile_pic' in request.FILES:
                profile.porfile_pic = request.FILES['porfile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                        {'user_form':user_form,
                        'profile_form':profile_form,
                        'registered':registered})

# Login functions starts from here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Accout not Active")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid login crediantials")
    else:
        return render(request,'basic_app/login.html',{})
