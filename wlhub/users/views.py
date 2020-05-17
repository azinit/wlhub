from django.contrib.auth import logout as _logout, authenticate, login
from django.shortcuts import render, redirect
from django.template.context_processors import csrf


def index(request):
    context = {}
    return render(request, 'users/index.html', context)


def sign_in(request):
    user = request.user
    context = {}
    context.update(csrf(request))

    if user.is_authenticated:
        return redirect("home-index")

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account-index')
        else:
            context["auth_error"] = "Invalid login or password"
    return render(request, 'sign-in/index.html', context)


def logout(request):
    _logout(request)
    return redirect('home-index')
