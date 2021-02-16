
from django.forms import ModelForm
from Profiles.models import createProfileModel

class createProfileForm(ModelForm):
    class Meta:
        model=createProfileModel
        fields="__all__"