from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price_on_book = models.DecimalField(decimal_places=0, max_digits=10)
    sell_price = models.DecimalField(decimal_places=0, max_digits=10)
    caption = models.TextField(blank=True)
    datetime_sell = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

