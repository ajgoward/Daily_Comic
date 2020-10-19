from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)

from products.models import Product
# Create your views here.


def see_the_bag(request):
    """ a view to return index """
    return render(request, "bag/thebag.html")


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
