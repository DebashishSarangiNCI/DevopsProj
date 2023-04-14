"""
accounts/forms.py: Module for user registration form.

This module defines the UserRegistrationForm, which is a form for user registration.
It includes fields for username, email, password, and password confirmation.
"""
from django import forms
from django.contrib.auth.models import User # noqa

class UserRegistrationForm(forms.Form):
    """
    UserRegistrationForm: A form for user registration.

    This form includes fields for username, email, password, and password confirmation.
    """
    username = forms.CharField(
        label='Username',
        max_length=100,
        min_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        max_length=35,
        min_length=5,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        max_length=50,
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        max_length=50,
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
