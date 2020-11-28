from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    food_genre = models.CharField(max_length=100)

    class PriceRange(models.TextChoices):
        one = "$"
        two = "$$"
        three = "$$$"
        four = "$$$$"

    price_range = models.CharField(max_length=4, choices=PriceRange.choices)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    address = models.ForeignKey(
        "address.Address",
        on_delete=models.SET_NULL,
        null=True
    )
    open_time = models.TimeField()
    close_time = models.TimeField()