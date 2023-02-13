from django.forms import ModelForm

from .models import Book


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'price_on_book',
            'sell_price',
            'caption',
        ]
