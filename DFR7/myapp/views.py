from django.shortcuts import render
from .serializer import Bookseri,Authorseri
from rest_framework import generics
from .models import Book,Author

# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=Authorseri

class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=Authorseri

    # Create your views here.
class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookseri

class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookseri