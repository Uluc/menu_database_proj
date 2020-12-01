from django.db import models
from django_mysql.models.fields import ListCharField


class Menu(models.Model):
    restaurant = models.ForeignKey("restaurant.Restaurant", on_delete=models.CASCADE)
    bio = models.TextField()


class Section(models.Model):
    title = models.CharField(max_length=15)
    menu = models.ForeignKey("menu.Menu", on_delete=models.CASCADE)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)


class Dish(models.Model):
    name = models.CharField(max_length=50)
    section = models.ManyToManyField("menu.Section")
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = ListCharField(base_field=models.CharField(max_length=15),
                                size=15,
                                max_length=(15 * 16))