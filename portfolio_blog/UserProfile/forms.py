from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Passowrd")
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    image = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, label='Type a description', max_length=250, required=False)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        
        if user.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        mail = User.objects.filter(email=email)
        
        if mail.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        
        if password_confirm != password:
            raise forms.ValidationError("Passwords must match.")
        return data




















