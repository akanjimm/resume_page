from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage

from resume_page.forms import ContactForm

def resume_view(request):
    form = ContactForm()
    context = {'form': form}

    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            comment = form.cleaned_data['comment']

            messages.add_message(request, messages.SUCCESS, "Successfully submitted! Thank you for getting in touch. Kindly check your email (including spam folder) for confirmation.")

            # sending email
            subject = "Appreciation"
            body = f"Hi {name}, \n\nThank you for getting in touch. It is much appreciated.\n\nYour response was successfully received.\n\nKind regards."

            email = EmailMessage(subject=subject, body=body, to=[email])
            email.send()
        
        else:
            form = ContactForm()

    return render(request, 'resume_page.html', context)