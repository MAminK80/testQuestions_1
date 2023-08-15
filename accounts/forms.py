from django import forms


class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Your Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': 'Your Password'}))