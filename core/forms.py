from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from db.models import CustomUser, LeaveRequest

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Your username',
		'class': "w-full py-4 px-6 rounded-xl"
	}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder':'Password',
		'class': "w-full py-4 px-6 rounded-xl"
	}))

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser  # User yerine CustomUser kullanıyoruz
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'status']  # Bu alanlar modelde olmalı
        
    def __init__(self, *args, **kwargs):
        super(LeaveRequestForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update({'class': 'datepicker'})
        self.fields['end_date'].widget.attrs.update({'class': 'datepicker'})