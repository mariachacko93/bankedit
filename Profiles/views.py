import random

from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView, FormView, DeleteView, TemplateView, RedirectView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView


# Create your views here.
from Profiles.forms import createProfileForm
from django.urls import reverse_lazy, reverse
from Profiles.models import createProfileModel, AccountInfoModel

from django.shortcuts import get_object_or_404


class CreateProfile(CreateView):
    form_class = createProfileForm
    # model=createProfileModel
    # fields="__all__"
    success_url = reverse_lazy('profilesuccess')
    template_name = "profiles/createprofile.html"

    def get_initial(self):
         return {'user': self.request.user}
def success(request):
    return render(request,"profiles/success.html")

def profilesuccess(request):
    return render(request,"profiles/profilesuccess.html")

class UpdateprofileView(UpdateView):
    model=createProfileModel
    fields = ["address","date_of_birth","email_id","phonenumber","branch"]
    # form_class = createProfileForm
    # fields = "__all__"
    success_url = reverse_lazy('home')
    template_name = "profiles/updateprofile.html"
# #
class Deleteprofile(DeleteView):
    model = User
    fields="__all__"
    success_url = reverse_lazy('homemain')
    template_name = "profiles/deleteprofile.html"


class ViewProfile(DetailView):
    model = createProfileModel
    fields="__all__"
    success_url = reverse_lazy('home')
    template_name = "profiles/viewprofile.html"


def randomGen():
    return int(random.uniform(100000, 999999))

def randomGen1():
    return int(random.uniform(1000, 9999))

def generateaccnoView(request):
    context = {}
    try:
        curr_user = AccountInfoModel.objects.get(username=request.user)  # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = AccountInfoModel()
        curr_user.accno = randomGen()  # random account number for every new user
        curr_user.mpin = randomGen1()
        curr_user.ifs_code = "HB1010010"
        curr_user.balance = 2000
        curr_user.username = request.user
        curr_user.save()
    return render(request, "profiles/generatesuccess.html", {"curr_user": curr_user})

class AccountView(DetailView):
    model = AccountInfoModel
    fields=["accno","mpin","balance"]
    success_url = reverse_lazy('home')
    template_name = "profiles/accountview.html"


