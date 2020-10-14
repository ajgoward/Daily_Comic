from django.shortcuts import render

# Create your views here.


def subscription(request):
    """ a view to return subscribe """
    return render(request, "subscriptions/subscribe.html")
