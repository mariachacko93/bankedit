import random

# from django.contrib.auth import logout
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, FormView, TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from Profiles.forms import createProfileForm,TransferForm,withdrawForm,BalanceForm
from django.urls import reverse_lazy
from Profiles.models import createProfileModel, AccountInfoModel,TransferModel
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CreateProfile(LoginRequiredMixin,CreateView):

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

class UpdateprofileView(LoginRequiredMixin,UpdateView):
    # login_url = 'login'
    model=createProfileModel
    fields = ["address","date_of_birth","email_id","phonenumber","branch"]
    success_url = reverse_lazy('home')
    template_name = "profiles/updateprofile.html"

class Deleteprofile(LoginRequiredMixin,DeleteView):
    model = User
    fields="__all__"
    success_url = reverse_lazy('homemain')
    template_name = "profiles/deleteprofile.html"


class ViewProfile(LoginRequiredMixin,DetailView):
    model = createProfileModel
    fields="__all__"
    success_url = reverse_lazy('home')
    template_name = "profiles/viewprofile.html"


def randomGen():
    return int(random.uniform(100000, 999999))

def randomGen1():
    return int(random.uniform(1000, 9999))

def generateaccnoView(request):
    try:
        curr_user = AccountInfoModel.objects.get(username=request.user)  # getting details of current user
    except:
        curr_user = AccountInfoModel()
        curr_user.accno = randomGen()  # random account number for every new user
        curr_user.mpin = randomGen1()
        curr_user.ifs_code = "HB1010010"
        curr_user.balance = 2000
        curr_user.username = request.user
        curr_user.save()
        # request.session["accno"]=curr_user.accno
        # request.session["mpin"]=curr_user.mpin
    return render(request, "profiles/generatesuccess.html", {"curr_user": curr_user})

class AccountView(LoginRequiredMixin,DetailView):
    model = AccountInfoModel
    fields=["accno","mpin","balance"]
    success_url = reverse_lazy('home')
    template_name = "profiles/accountview.html"


class balanceEnquiry(DetailView):
    model = AccountInfoModel
    fields = ["balance"]
    # success_url = reverse_lazy('home')
    template_name = "profiles/balance.html"



class TransferView(LoginRequiredMixin,View):
    # model = TransferModel
    form=TransferForm()
    fields=["accno","amount","mpin"]
    template_name = "profiles/accounttransfer.html"
    context = {}

    def get_initial(self):
        return {'user': self.request.user}

    def get(self, request, *args, **kwargs):

        form=TransferForm()
        self.context["form"]=form
        return render(request, self.template_name, self.context)



    def post(self, request, *args, **kwargs):
        form=TransferForm(request.POST)
        self.context={}
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            accno = form.cleaned_data.get("accno")
            try:
                object = AccountInfoModel.objects.get(mpin=mpin)
                bal = object.balance - amount
                object.balance = bal
                object.save()
                object1 = AccountInfoModel.objects.get(accno=accno)
                bal1 = object1.balance + amount
                object1.balance = bal1
                object1.save()
                self.context["amount"]=amount
                self.context["accno"]=object1

            except Exception:

                self.context["form"] = form
                return render(request, self.template_name, self.context)
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()


            # form.save()
            return render(request, "profiles/transfersuccess.html", self.context)

            # return redirect("transfers")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

@login_required
def transfersuccess(request):
    return render(request,"profiles/transfersuccess.html")

class withdrawView(LoginRequiredMixin,View):
    # model = TransferModel
    form = withdrawForm()
    fields = [ "amount", "mpin","user"]

    def get_initial(self):
        return {'user': self.request.user}

    template_name = "profiles/withdraw.html"
    context = {}


    def get(self, request, *args, **kwargs):
        form=withdrawForm()
        self.context["form"]=form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context={}
        form=withdrawForm(request.POST)
        if form.is_valid():
                mpin = form.cleaned_data.get("mpin")
                amount = form.cleaned_data.get("amount")
                try:
                    object = AccountInfoModel.objects.get(mpin=mpin)
                    bal = object.balance - amount
                    object.balance = bal
                    object.save()
                    self.context["amount"]=amount

                except Exception:
                    self.context["form"] = form
                    return render(request, self.template_name, self.context)

                # not null error
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                # form.save()
                return render(request,"profiles/withdrawsuccess.html", self.context)

                # return redirect("home")
        else:
                self.context["form"] = form
                return render(request, self.template_name, self.context)

@login_required
def withdrawsuccess(request):
    return render(request,"profiles/withdrawsuccess.html")

class DepositView(LoginRequiredMixin,View):
    # model = TransferModel()
    form = TransferForm()
    fields = ["amount", "mpin","user"]
    template_name = "profiles/deposit.html"
    context = {}

    def get_initial(self):
        return {'user': self.request.user}

    def get(self, request, *args, **kwargs):
        form=withdrawForm()
        self.context["form"]=form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        self.context={}
        form=withdrawForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            amount = form.cleaned_data.get("amount")
            # date=form.cleaned_data.get("date")

            try:
                object = AccountInfoModel.objects.get(mpin=mpin)
                bal = object.balance + amount
                object.balance = bal
                object.save()
                self.context["amount"] = amount

            except Exception:
                self.context["form"] = form
                return render(request, self.template_name, self.context)

            # code for not null :assigning to another variable
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            # form.save()
            return render(request, "profiles/depositsucces.html", self.context)

            # return redirect("home")
        else:
                self.context["form"] = form
                return render(request, self.template_name, self.context)

        # return render(request, self.template_name, self.context)

@login_required
def depositsuccess(request):
    return render(request,"profiles/depositsuccess.html")

class accountActivity(ListView):
    model=TransferModel
    # form_class=TransferForm
    # fields=["accno","amount","date","user"]
    fields="__all__"

    template_name = "profiles/activity.html"

    def get_initial(self):
         return {'user': self.request.user}

    def get_queryset(self):
        context={}
        mpin=AccountInfoModel.objects.get(username=self.request.user).mpin
        # print(type(mpin))
        return TransferModel.objects.filter(mpin=mpin)
        # context["trans"]=trans
        # return render(request,"profiles/activity.html",context)

