from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('bag', {})

    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))
    form = OrderForm()
    context = {
        'form': form,
        'basket': basket
    }
    template = 'checkout/checkout.html'
    return render(request, template, context)
