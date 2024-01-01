from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Book


# Create your views here.
class BookCreate(CreateView):
    model = Book
    fields = [
        "title",
        "author",
        "abstract",
        "price"
    ]

    success_url = "/"


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


class BookUpdate(UpdateView):
    model = Book
    fields = [
        "title",
        "author",
        "abstract",
        "price"
    ]

    success_url = "/"


class BookDelete(DeleteView):
    model = Book

    success_url = "/"
