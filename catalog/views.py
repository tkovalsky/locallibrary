from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.order_by('last_name')

class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'


def index(request):
    """
    View function for the home page of this site
    """
    #Generate counts for some main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count() #'All' is implied by default

    #Render the html template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
        },
    )
