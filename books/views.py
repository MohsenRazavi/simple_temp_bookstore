from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import AddBookForm


def book_list_view(request):
    books = Book.objects.all().order_by('-datetime_sell')
    sum_money = 0
    for book in books:
        sum_money += book.sell_price
    return render(request, 'books/book_list_view.html',
                  context={'books': books, 'sum_of_money': sum_money, 'add_book_form': AddBookForm, })


class BookAddView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = AddBookForm
    success_url = reverse_lazy('home')


@login_required
def book_delete_view(request, pk):
    book = Book.objects.filter(pk=pk)
    book.delete()
    return redirect(reverse_lazy('home'))
