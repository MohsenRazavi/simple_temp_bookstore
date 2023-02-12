from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price_on_book = models.DecimalField(decimal_places=2, max_digits=10)
    sell_price = models.DecimalField(decimal_places=2, max_digits=10)
    caption = models.TextField(blank=True)


