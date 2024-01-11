from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length = 255)
    class Meta:
        db_table='items'