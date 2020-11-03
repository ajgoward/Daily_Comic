from django.shortcuts import (
    render, redirect, reverse, HttpResponse, HttpResponseRedirect)


# Create your views here.


def see_the_bag(request):
    """ A view that renders the baasket contents page """

    return render(request, 'bag/thebag.html')


def quick_add(request, item_id):
    """ for the quick add button on the product page first set
    the quantity and then change to 1 to add to basket
    """
    quantity = 0
    basket = request.session.get('bag', {})
    if quantity == 0:
        quantity = 1

        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['bag'] = basket
    """recieved this from stackoverflow
    https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django
    to redirect to page the user
    was one origionally instead of going back to default product page"""
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('bag', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
            else:
                basket[item_id]['items_by_size'][size] = quantity
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['bag'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    basket = request.session['bag']
    quantity = 0

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['bag'] = basket
    print("this is working")
    return redirect(reverse('home'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('bag', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['bag'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(e, status=500)
