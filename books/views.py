from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from models import Book


class BookListView(generic.ListView):
    model = Book
    # template_name = ''


class BookAddView(generic.CreateView):
    model = Book
    success_url = reverse_lazy('home')


class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('home')

