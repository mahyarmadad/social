from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreateForm
from .models import User

# Create your views here.


class Home(TemplateView):
    template_name = "index.html"


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class SignoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(
                request, "Thank you " f'{request.user.username} , for spending some quality time with us hope to see you Again')
        else:
            messages.error(
                request, f'{request.user.username} your error message')
        return super().dispatch(request, *args, **kwargs)


class SigninView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = "You successfully logged in"
