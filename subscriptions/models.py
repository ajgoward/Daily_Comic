from django.db import models


class Subscriptions(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Recurring = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    stripePricekey = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
