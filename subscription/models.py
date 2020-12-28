from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=254)
    sub_id = models.CharField(max_length=254, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image_url = models.URLField(
        max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
