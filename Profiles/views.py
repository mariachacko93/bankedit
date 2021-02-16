from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, FormView, DeleteView, TemplateView
from django.views.generic.edit import UpdateView

# Create your views here.
from Profiles.forms import createProfileForm
from django.urls import reverse_lazy
from Profiles.models import createProfileModel

from django.shortcuts import get_object_or_404


class CreateProfile(CreateView):
    form_class = createProfileForm
    success_url = reverse_lazy('home')
    template_name = "profiles/createprofile.html"


def success(request):
    return render(request,"profiles/success.html")

#
class UpdateprofileView(UpdateView):
    model=createProfileModel
    fields = "__all__"
#     # form_class = createProfileForm
    success_url = reverse_lazy('home')
    template_name = "profiles/updateprofile.html"
# #
#
class Deleteprofile(DeleteView):
    model = createProfileModel
    fields="__all__"
    success_url = reverse_lazy('home')
    template_name = "profiles/deleteprofile.html"



# class UpdateprofileView(UpdateView):
#     model=createProfileModel
#     fields="__all__"
#     template_name = "profiles/updateprofile.html"
#     success_url = reverse_lazy('home')
#
#     def get_query_set(self,pk):
#         return self.model.objects.get(pk=pk)

