from django.contrib.auth import logout as _logout, authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.template.context_processors import csrf


def index(request):
    context = {}
    return render(request, 'users/index.html', context)


def sign_in(request):
    user = request.user
    context = {}
    errors = []
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
        errors.append("Invalid login or password")

    context["auth_errors"] = errors
    return render(request, 'sign-in/index.html', context)


def sign_up(request):
    user = request.user
    context = {}
    context.update(csrf(request))
    errors = []

    if user.is_authenticated:
        return redirect("home-index")

    if request.POST:
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # FIXME: simplify
        # validating
        email_exists = get_user_model().objects.filter(email=email).exists()
        username_exists = get_user_model().objects.filter(username=username).exists()

        if not email_exists and not username_exists:
            # creating new user
            user = get_user_model().objects.create(
                username=username,
                email=email,
                password=password
            )
            # hashing
            user.set_password(password)
            user.save()
            return redirect("account-sign-in")

        # process errors
        if email_exists:
            errors.append('Such email is already taken')
        if username_exists:
            errors.append('Such username is already taken')

    context["auth_errors"] = errors
    return render(request, 'sign-up/index.html', context)


def logout(request):
    _logout(request)
    return redirect('home-index')
