from django.shortcuts import render


def theProfile(request):
    template = 'profiles/theprofile.html'

    return render(request, template)
