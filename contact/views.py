from django.core.mail import send_mail
from django.shortcuts import render

from django.conf import settings

from .forms import ContactForm
from .models import Contact


def contact(request):
    is_submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_message = form.cleaned_data["user_message"]
            user_email = form.cleaned_data["user_email"]

            from config.models import MainConfig
            main_config = MainConfig.get_solo()
            raw_email = main_config.email_adresse
            
            # Format custom obfuscated email strings (e.g. [@] and [dot]) to standard emails
            recipient_email = raw_email.replace(" [@] ", "@").replace(" [dot] ", ".").replace("[@]", "@").replace("[dot]", ".")

            new_contact = Contact(
                name=user_name,
                message=user_message,
                email=user_email,
            )
            new_contact.save()

            if settings.EMAIL_NOTIFICATION:
                try:
                    send_mail(
                        "DevCase: new message via contact page",
                        f"Message:{user_message} | Author: {user_name} | Email: {user_email}",
                        settings.DEFAULT_FROM_EMAIL,
                        [recipient_email],
                        fail_silently=False,
                    )
                except Exception as e:
                    # Catch all SMTP errors so the form submission doesn't crash on Vercel
                    print(f"Failed to send email notification: {e}")

            is_submitted = True
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        "form": form,
        "is_submitted": is_submitted,
    }

    return render(request, "contact.html", context=context)
