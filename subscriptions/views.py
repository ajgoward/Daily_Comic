from django.shortcuts import render
from .models import Subscriptions

# Create your views here.


def subscription(request):
    """ a view to return subscribe """
    subscriptions = Subscriptions.objects.all()
    template = "subscriptions/subscribe.html"

    context = {
        'subscrip': subscriptions,
    }
    return render(request, template, context)
