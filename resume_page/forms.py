from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=255)
    phone_number = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea)
