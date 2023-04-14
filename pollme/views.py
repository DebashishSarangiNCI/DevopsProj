from django.shortcuts import render


def home(request):
    """
    View for rendering the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered home page.
    """
    return render(request,'home.html')