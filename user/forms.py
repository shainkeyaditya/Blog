from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="User name")
    password = forms.CharField(max_length=22, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=22, label="Verify Password", widget=forms.PasswordInput)

