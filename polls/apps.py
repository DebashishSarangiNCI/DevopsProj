from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    AppConfig for the 'polls' app.

    This AppConfig class represents the configuration for the 'polls' app
    in a Django project. It is used to configure various aspects of the app,
    such as the app's name, label, and any app-specific settings.

    Attributes:
        name (str): The name of the app, which is used as its unique identifier
            in the Django project.

    """
    name = 'polls'
