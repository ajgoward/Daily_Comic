from django.shortcuts import render


def homepage(request):
    """ a view to return index """
    return render(request, "home/index.html")
