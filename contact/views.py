from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(
                sender_name, form.cleaned_data['message'])
            send_mail(
                'New Enquiry', message, sender_email, [
                    'enquiry@DailyComic.com'])
            messages.info(
                request, 'Successfully sent your message! \
                     Thank You! Our team will be in touch \
                          within the next 48hours')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "contact/contactus.html", context)
