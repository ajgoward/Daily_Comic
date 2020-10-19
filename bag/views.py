from django.shortcuts import render

# Create your views here.


def see_the_bag(request):
    """ a view to return index """
    return render(request, "bag/thebag.html")
