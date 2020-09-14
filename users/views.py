from django.contrib.auth import logout as _logout, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import FormView

from users.forms import UserForm, UserSurveyForm


@login_required
def index(request):
    context = {}
    return render(request, 'users/index.html', context)


@login_required
def settings(request):
    context = {}
    context["form"] = UserForm(instance=request.user)
    if request.POST:
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("account-index")
        else:
            context["errors"] = ["Неверно заполнена форма. Проверьте введенные данные."]
    return render(request, 'users/settings.html', context)


class SurveyForm(LoginRequiredMixin, FormView):
    template_name = "users/survey.html"
    form_class = UserSurveyForm
    success_url = reverse_lazy("account-index")

    def form_valid(self, form):
        survey = form.save(commit=False)
        survey.rate = int(self.request.POST["rating"])
        survey.user = self.request.user
        survey.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error("Ошибка заполнения формы", "Проверьте введенные данные")
        return super().form_invalid(form)


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
        errors.append("Неверный логин или пароль")

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
