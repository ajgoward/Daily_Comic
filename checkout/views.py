from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

from bag.contexts import basket_contents
import stripe



def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = ''
    print(stripe_secret_key)
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    grand_total = current_basket['grand_total']
    stripe_total = round(grand_total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )



    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'form': order_form,
        'stripe_public_key': '',
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
