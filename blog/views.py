from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


def enter(request):
    return render(request, 'account/initial.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect("blog:index")


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            user_form_errors = None
            profile_form_errors = None
        else:
            user_form_errors = user_form.errors
            profile_form_errors = profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        user_form_errors = None
        profile_form_errors = None
    return render(request, 'account/registration.html', {'user_form': user_form, 'profile_form': profile_form,
                'registered': registered, 'user_errors': user_form_errors, 'profile_errors': profile_form_errors})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("blog:index")
        else:
            user = None
            return render(request, 'account/login.html', {'error_message': "Invalid login details given.\nLogin failed."})

    else:
        user = None
        return render(request, 'account/login.html', {'error_message': None})

