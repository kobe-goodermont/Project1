import form
from django.forms import ModelForm
from Project1_app.models import Workout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Workout


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

        widgets= {
            'TITLE': forms.TextInput(attrs={'class': 'form-control'}),
            'DESCRIPTION': forms.Textarea(attrs={'class': 'form-control'}),
            'GROUP': forms.Select(attrs={'class': 'form-control'}),
        }


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

