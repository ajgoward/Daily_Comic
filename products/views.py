from django.shortcuts import render


def all_stock(request):

    return render(request, 'products/products.html')
