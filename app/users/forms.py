from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserSignUpForm(UserCreationForm):
    
    email = forms.EmailField(label=_('Elektron pochta'), 
                             widget=forms.EmailInput(attrs={'id': 'email', 
                                                            'placeholder': _('Elektron pochta')}),
                             required=True) 
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Parol')}), 
                                required=True)
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Parolni tasdiqlang')}), 
                                required=True)
    
    receive_email = forms.BooleanField(label=_('Yes, I would like to receive the monthly newsletter. I may unsubscribe at anytime.'),
                                       required=False, 
                                       widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'receive_email'}))

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password1', 'password2', 'receive_email']




class UserSignInForm(forms.Form):

    email = forms.EmailField(label=_('Elektron pochta'), 
                             required=True, 
                             widget=forms.TextInput(attrs={'id': 'email',
                                                           'placeholder': _('Elektron pochta')})) 
    
    password = forms.CharField(label='Password',
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': _('Parol'),
                                                                 'id': 'password'}))