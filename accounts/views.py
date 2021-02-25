from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from Profiles.models import createProfileModel
from accounts.forms import RegistrationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, View, FormView, UpdateView, RedirectView


class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Signin(LoginView):
    def get(self, request):
        if request.method == "GET":
            if (User.objects.filter(username=request.GET.get("username"), password=request.GET.get("password"))).exists():
                user = User.objects.get(username=request.GET.get("username"), password=request.GET.get("password"))
                request.session["user"] = user.id
        return render(request, 'accounts/signin.html', { 'form':  AuthenticationForm })

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is None:
                return redirect("signup")

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(request,'accounts/signin.html', { 'form': form, 'invalid_creds': True })


            login(request, user)
            return redirect(reverse('home'))


        return render(request, 'accounts/signin.html', {'form': form, 'invalid_creds': True})


# def Homepage(request):
#     return render(request,"accounts/home.html")

class Homepage(LoginRequiredMixin,View):
    template_name = 'accounts/home.html'
    def get(self, request):
        context={}

        try:
            uid= User.objects.get(username=request.user).id
            # print(uid,type(uid))
        except:
            uid=None
        context = {'uid': uid}
        return render(request, 'accounts/home.html', context)



def Homepagemain(request):
    return render(request,"accounts/homemain.html")



def SignOutView(request):
    logout(request)
    return render(request,"accounts/homemain.html")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            auth.logout(request)
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
