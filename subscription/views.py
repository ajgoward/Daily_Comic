from django.shortcuts import render, get_object_or_404
from profiles.models import Userprofiles
from profiles.forms import ProfileForm
from django.conf import settings
import stripe
from .models import Subscription


# Create your views here.
def subscription(request):
    subscription = Subscription.objects.all()

    context = {
        'subscription': subscription,
    }

    return render(request, "subscription/subs.html", context)


def make_subscription(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key
    profile = get_object_or_404(Userprofiles, user=request.user)
    template = "subscription/makesub.html"
    form = ProfileForm(instance=profile)
    context = {
        'stripe_public_key': stripe_public_key,
        'form': form,
        'on_profile': True,
    }
    return render(request, template, context)
