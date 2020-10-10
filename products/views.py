from django.shortcuts import render, get_object_or_404
from .models import Product


def all_stock(request):

    products = Product.objects.all

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def item_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/item-detail.html', context)
