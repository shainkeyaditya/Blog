from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="User name")
    password = forms.CharField(max_length=22, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=22, label="Verify Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm != confirm:
            raise forms.ValidationError("Passwords do not match")

        values = {
            "username" : username,
            "password" : password
        }
        return values