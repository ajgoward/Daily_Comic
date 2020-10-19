from django.shortcuts import render, redirect

# Create your views here.


def see_the_bag(request):
    """ A view that renders the baasket contents page """

    return render(request, 'bag/thebag.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    quantity = 0

    if quantity == 0:
        quantity = 1
    else:
        quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('bag', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['bag'] = basket
    return redirect(redirect_url)
