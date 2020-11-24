from django.shortcuts import render, get_object_or_404

from .models import Userprofiles


def theProfile(request):
    profile = get_object_or_404(Userprofiles, user=request.user)
    template = 'profiles/theprofile.html'
    context = {
        'profile': profile
    }
    return render(request, template, context)
