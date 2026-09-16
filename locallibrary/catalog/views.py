from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    print("num_visits" + str(num_visits))
    num_visits += 1
    print("num_visits after incrementing:" + str(num_visits))
    request.session['num_visits'] = num_visits
    print("num_visits in session:" + str(request.session['num_visits']))

    # counts for genres and books that contain a particular word
    num_fiction_genres = Genre.objects.filter(name__contains='Fiction').count()
    num_ninth_books = Book.objects.filter(title__contains='Ninth').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fiction_genres': num_fiction_genres,
        'num_ninth_books': num_ninth_books,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 1

class AuthorListView(generic.ListView):
    model= Author
    paginate_by = 1

class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by = 1