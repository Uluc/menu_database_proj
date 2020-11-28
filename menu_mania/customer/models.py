from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    address = models.ForeignKey("address.Address", on_delete=models.PROTECT)
