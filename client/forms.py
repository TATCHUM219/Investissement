
from django.forms import ModelForm, TextInput, NumberInput, PasswordInput, EmailInput
from .models import *


# Create your forms here


class deposit_form(ModelForm):
    class Meta:
        model = Depot
        fields = ['montant', 'client']
        widgets = {
            'montant' : NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Amount to invest', 'required' : ''}),
            'client' : TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter the payer address', 'required' : ''})
        }

class withdrawal_form(ModelForm):
    class Meta:
        model = Retrait
        fields = ['montant', 'client']
        widgets = {
            'montant' : NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Amount to withdraw', 'required' : ''}),
            'client' : TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter the receiver address', 'required' : ''})
        }

class clientSettings(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ('refferal_bonus', 'checkbox', 'email') 
        widgets = {
            'nom' : TextInput(attrs={'class' : 'form-control form-control-lg', 'id' : 'display-name', 'placeholder' : 'Enter your name', 'required' : 'false'}),
            'telephone' : NumberInput(attrs={'class' : 'form-control form-control-lg', 'id' : 'phone-no', 'placeholder' : 'Enter your phone number', 'required' : 'false'}),
            'email' : EmailInput(attrs={'class' : 'form-control form-control-lg', 'id' : 'email', 'placeholder' : 'Enter your email address', 'required' : ''}),
            # 'checkbox' : CheckboxInput(attrs={'class' : 'custom-control-input', 'id' : 'checkbox', 'required' : ''}),
            
            # 'user_dad' : TextInput(attrs={'class' : 'form-control form-control-lg', 'id' : 'user_dad', 'placeholder' : 'Fill your refferal id', 'required' : ''}),
        }

class userAccountSettings(ModelForm):
    class Meta:
        model = Compte
        fields = ['password']
        widgets = {
            'password' : PasswordInput(attrs={'class' : 'form-control form-control-lg', 'id' : 'password', 'placeholder' : '********************', 'required' : ''}),
        }