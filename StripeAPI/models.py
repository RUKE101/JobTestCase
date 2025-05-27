from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=512, blank=False, null=False)
    price = models.PositiveIntegerField()
