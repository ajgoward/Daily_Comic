from django.db import models


class Subscriptions(models.Model):
    Name = models.CharField(max_length=255)
    image_url = models.URLField(
        max_length=1024, blank=True)
    image = models.ImageField(blank=True)
    Description = models.CharField(max_length=255)
    Recurring = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stripeSubscriptionId = models.CharField(max_length=255)
    stripePricekey = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
