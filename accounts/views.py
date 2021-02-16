from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from accounts.forms import RegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,View,FormView,UpdateView


class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Signin(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signin.html'

def Homepage(request):
    return render(request,"accounts/home.html")

def Homepagemain(request):
    return render(request,"accounts/homemain.html")

