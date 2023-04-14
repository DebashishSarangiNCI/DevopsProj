from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponse

"""
views.py: This module contains views for the accounts app.

This module includes views for handling user authentication and registration in the
accounts app. It uses Django's built-in authentication system and renders templates
to display login and registration forms. It also validates form data, performs
authentication, and handles registration. The views are responsible for rendering
HTML templates, performing authentication tasks, and redirecting users to appropriate
pages after successful login or registration. The views in this module are used in
conjunction with URL patterns defined in the `urls.py` module to handle incoming
HTTP requests related to user authentication and registration in the accounts app.
"""


def login_user(request):
     """
    View for handling user login.

    This view handles the logic for authenticating user credentials entered in the
    login form. If the form data is valid and the user exists, it logs in the user and
    redirects to the next URL specified in the 'next' parameter in the query string,
    or to the home page if 'next' is not specified. If the form data is invalid or
    the user does not exist, it displays an error message on the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the login page or a redirect
        response to the next URL or home page.

    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, "Username Or Password is incorrect!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'accounts/login.html')


def logout_user(request):
       """
    View for handling user logout.

    This view handles the logic for logging out the currently logged-in user and
    redirecting to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with a redirect response to the home page.

    """
    logout(request)
    return redirect('home')


def create_user(request):
    """
    View for handling user registration.

    This view handles the logic for registering a new user. It validates the form data
    submitted in the registration form, performs checks for password match, existing
    username, and existing email, and creates a new user if all checks pass. It displays
    appropriate error messages on the registration page if any checks fail.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the registration page or a redirect
        response to the login page.

    """
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            if password1 != password2:
                check1 = True
                messages.error(request, 'Password did not match!',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(request, 'Username already exists!',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(request, 'Email already registered!',
                               extra_tags='alert alert-warning alert-dismissible fade show')

            if check1 or check2 or check3:
                messages.error(
                    request, "Registration Failed!", extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                messages.success(
                    request, f'Thanks for registering {user.username}.', extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
