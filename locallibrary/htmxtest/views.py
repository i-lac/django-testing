from django.shortcuts import render

# Create your views here.

def htmxhome(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'htmxhome.html', context={})

def sandwich(request):
    """View function for sandwich request."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sandwich.html', context={'response': '🥪 yum'})

from django.http import HttpResponse

def hello(request):
    return HttpResponse("<p>Hello from Django!</p>")
