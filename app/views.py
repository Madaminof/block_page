from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from app.models import Category, Detail
from django.views.generic import DeleteView, ListView


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("category")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    return render(request, 'home.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "registration.html"


# views.py

from django.views.generic import ListView
from .models import Category


class CategoryView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'





class DetailView(DeleteView):
    model = Detail
    template_name = 'detail.html'
    context_object_name = 'detail'
