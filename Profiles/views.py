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
from Profiles.models import createProfileModel

from django.shortcuts import get_object_or_404


class CreateProfile(CreateView):
    form_class = createProfileForm
    # model=createProfileModel
    # fields="__all__"
    success_url = reverse_lazy('home')
    template_name = "profiles/createprofile.html"

    def get_initial(self):
         return {'user': self.request.user}
def success(request):
    return render(request,"profiles/success.html")

class UpdateprofileView(UpdateView):
    model=createProfileModel
    fields = ["address","date_of_birth","email_id","phonenumber"]
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


# class UpdateprofileView(UpdateView):
#     model=createProfileModel
#     fields="__all__"
#     template_name = "profiles/updateprofile.html"
#     success_url = reverse_lazy('home')
#
#     def get_query_set(self,pk):
#         return self.model.objects.get(pk=pk)

