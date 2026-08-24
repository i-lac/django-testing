from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# These lines simply register the models with the admin site, so that they can be managed through the Django admin interface.
admin.site.register(Genre)
admin.site.register(Language)



# The following lines allow for customisation of the admin interfaces for all the other models I want to register

# AUTHOR REGISTRATION
# This class defines the inline admin interface for the Book model, which acts as a child model to the Author model. 
# It allows for the display of related Book instances directly within the "add Author"/"detail view of Author" admin pages.
class BookInline(admin.TabularInline):
    model = Book
    extra = 0

# Define the admin class for the Author model
class AuthorAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view of the Author model in the admin interface
    # Otherwise would just display the __str__() method of the model, which is just the name of the author
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # Define the fields to be displayed in the detail view of the Author model in the admin interface
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    # This line adds the BookInline class to the AuthorAdmin class, allowing for the display of related Book instances directly within the "add Author"/"detail view of Author" admin pages.
    inlines = [BookInline]

# Register the admin class with the associated model
# This is one registration method, but there is another (see below)
admin.site.register(Author, AuthorAdmin)


# BOOK REGISTRATION
# Same deal with the inline stuff
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0   

# Register the Admin classes for Book using the decorator (other registration method)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # display_genre is a method defined in the Book model that returns a string representation of the genres associated with a book.
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


# BOOK INSTANCE REGISTRATION
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    # Define the fieldsets for the detail view of the BookInstance model in the admin interface
    # Honestly just run the server, access the admin interface for book instances and compare the 
    # "add new book instance" page to this list to see what this does, it's a bit hard to explain in words
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )