from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry: " + form.cleaned_data["subject"]
            body = (
                f"Inquiry from {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
                f" ({form.cleaned_data['email_address']}):\n{form.cleaned_data['message']}"
            )
            try:
                send_mail(subject, body, form.cleaned_data["email_address"], [settings.EMAIL_SEND_TO])
            except BadHeaderError:
                return HttpResponse("Invalid header found.", status=400)
            messages.success(request, "Message sent")
            return redirect("/contact")
        else:
            messages.error(request, "Failed to send message")
            return redirect("/contact")

    form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})
