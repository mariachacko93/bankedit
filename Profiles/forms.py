
from django.forms import ModelForm
from Profiles.models import createProfileModel
from django import forms

class createProfileForm(ModelForm):
    # user = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model=createProfileModel
        fields="__all__"
        widgets={"user":forms.HiddenInput(),}