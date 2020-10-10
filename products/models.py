from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    universe = models.CharField(max_length=254, blank=True)
    hero = models.CharField(max_length=254, blank=True)
    author = models.CharField(max_length=254, blank=True)
    artist = models.CharField(max_length=254, blank=True)
    publishedby = models.CharField(max_length=254, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    rrp = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True)
    image_url = models.URLField(
        max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name