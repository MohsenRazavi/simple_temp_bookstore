from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = [
        'name',
        'price_on_book',
        'sell_price',
        'datetime_sell',
    ]
