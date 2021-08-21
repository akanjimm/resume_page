from django.shortcuts import render
from resume_page.forms import ContactForm
from django.contrib import messages

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

            messages.add_message(request, messages.SUCCESS, "Successfully submitted! Thank you for getting in touch.")
        
        else:
            form = ContactForm()

    return render(request, 'resume_page.html', context)

