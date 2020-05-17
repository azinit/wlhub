from django.contrib.auth import logout as _logout, authenticate, login
from django.shortcuts import render, redirect


def index(request):
    context = {}
    return render(request, 'users/index.html', context)


def sign_in(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home-index")

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account-index')
            # Redirect to a success page.
            pass
        else:
            # Return an 'invalid login' error message.
            pass
    context = {}
    return render(request, 'sign-in/index.html', context)


def logout(request):
    _logout(request)
    return redirect('home-index')
