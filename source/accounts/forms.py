from django import forms


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', required=True)
    password = forms.CharField(max_length=100, label='Password', required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='Password Confirm', required=True, widget=forms.PasswordInput)

