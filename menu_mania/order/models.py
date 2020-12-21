from django.db import models
from django.forms.models import model_to_dict


class Cart(models.Model):
    restaurant = models.ForeignKey(
        "restaurant.Restaurant",
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        "customer.Customer",
        on_delete=models.CASCADE
    )
    time_ordered = models.DateTimeField(auto_now=True)
    # dish = models.ManyToManyField("menu.Dish")
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    tip = models.DecimalField(max_digits=7, decimal_places=2, default=0)



    def save(self, *args, **kwargs):
        # sum of all the dishes
        cost = sum([item.calc() for item in self.purchase_set.all()])
        # tip
        cost += tip
        # tax
        cost *= 1.1
        self.cost = cost
        super(Cart, self).save(*args, **kwargs)


class Purchase(models.Model):
    cart = models.ForeignKey('order.Cart', on_delete=models.CASCADE)
    dish = models.ForeignKey('menu.Dish', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def calc(self):
        cost = self.dish.cost * self.quantity
        return cost
