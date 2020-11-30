from django.db import models


class Order(models.Model):
    restaurant = models.ForeignKey(
        "restaurant.Restaurant",
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        "customer.Customer",
        on_delete=models.CASCADE
    )
    time_ordered = models.DateTimeField(auto_now=True)
    time_delivered = models.DateTimeField()
    dish = models.ManyToManyField("menu.Dish")
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)