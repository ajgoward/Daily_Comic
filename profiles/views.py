from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Userprofiles
from .forms import ProfileForm

def theProfile(request):
    profile = get_object_or_404(Userprofiles, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully updated your details!')
            
    orders = profile.orders.all()
    template = 'profiles/theprofile.html'
    form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'orders': orders,
        'on_profile': True,
    }
    return render(request, template, context)
