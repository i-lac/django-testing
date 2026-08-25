from django.shortcuts import render

# Create your views here.

has_sandwich = False

def htmxhome(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'htmxhome.html', context={})

def sandwich(request):
    """View function for sandwich request."""

    global has_sandwich
    has_sandwich = True
    print('sending over the sandwich!')

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sandwich.html', context={'sandwich': '🥪 yum'})

def check_sandwich(request):
    """View function for checking if sandwich is available."""

    global has_sandwich
    if has_sandwich:
        print('has sandwich yes!')
        return render(request, 'check_sandwich.html', context={'sandwich_status': 'yes :) yay'})
    else:
        print('no sandwich! aaaahhhhh!!!!!!')
        return render(request, 'check_sandwich.html', context={'sandwich_status': 'no TT_TT what the flip...'})

from django.http import HttpResponse

def hello(request):
    return HttpResponse("<p>Hello from Django!</p>")

def submit_form(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        greeting = f"Hello, {name}!"
        return HttpResponse(f"<p>{greeting}</p>")
    return HttpResponse("<p>Please enter your name.</p>")

