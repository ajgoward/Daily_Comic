from django.shortcuts import render, redirect

# Create your views here.


def see_the_bag(request):
    """ A view that renders the baasket contents page """

    return render(request, 'bag/thebag.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    quantity = 0
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

        if quantity == 0:
            quantity = 1
        else:
            quantity = int(request.POST.get('quantity'))

        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['bag'] = basket
    return redirect(redirect_url)
