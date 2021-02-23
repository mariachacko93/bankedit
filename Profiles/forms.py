
from django.forms import ModelForm, DateInput
from Profiles.models import createProfileModel,AccountInfoModel,TransferModel
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class createProfileForm(ModelForm):
    # user = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model=createProfileModel
        fields="__all__"
        widgets={"user":forms.HiddenInput(),
                 "email_id": forms.EmailInput(),
                 'date_of_birth': DateInput()}

# class DepositForm(ModelForm):
#     class Meta:
#         model=AccountInfoModel
#         fields=[""]

class TransferForm(ModelForm):
    # user = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model=TransferModel
        fields="__all__"
        widgets={
                 "mpin": forms.PasswordInput(),}

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        accno=cleaned_data.get("accno")
        amount=cleaned_data.get("amount")
        print(mpin,",",accno,",",amount)
        try:
            object=AccountInfoModel.objects.get(mpin=mpin)
            if(object):

        # for checking sufficent balance
                if(object.balance<amount ):
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)
        # for account validation
        try:
            object=AccountInfoModel.objects.get(accno=accno)
            if(object):
                pass
        except:
            msg="you have provided invalid accno"
            self.add_error("accno",msg)


class withdrawForm(ModelForm):
    class Meta:
        model = TransferModel
        fields =["amount","mpin"]
        widgets={
                 "mpin": forms.PasswordInput(),}


class depositForm(ModelForm):
    class Meta:
        model = TransferModel
        fields =["amount","mpin"]
        widgets={
                 "mpin": forms.PasswordInput(),}