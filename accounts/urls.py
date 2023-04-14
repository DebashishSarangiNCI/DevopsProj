"""
urls.py: This module contains URL patterns for the accounts app.

This module includes URL patterns for the accounts app, which define the routing
and mapping of URLs to the corresponding views. The `path` function from Django's
`urls` module is used to define the URL patterns. The views from the `views` module
in the same app are imported and associated with the URL patterns. The `app_name`
variable is set to "accounts" to specify the namespace for the app, which allows
for namespacing of URLs in Django apps. This module serves as the entry point for
defining URL patterns for the accounts app and routing incoming requests to the
appropriate views.
"""
from django.urls import path
from . import views


app_name = "accounts"

urlpatterns=[
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),
]
