from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text_input',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'text_input',
        'placeholder': 'Password',
    }))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'text_input',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={
        'class': 'text_input',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'First name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'text_input',
                'placeholder': 'Email'
            }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] == cd['password2']:
            return cd['password2']
        raise forms.ValidationError('Passwords don\'t match.')
