from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from django.core.mail.message import EmailMessage
from django.contrib.auth.models import AbstractUser

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome',
        min_length=3,
        max_length=50,
        help_text="Usuário Preenchimento Obrigatório",
    )
    password = forms.CharField(
        label='Password',
        help_text="Senha Preenchimento Obrigatório",
        required=True,
        widget=forms.PasswordInput
    )

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Senha incorreta.')
        return cd['password2']

    def clean_email(self):
       email = self.cleaned_data.get('email')
       cd = self.cleaned_data
       if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já Existe.')
       return cd['email']