
from django import forms

# from .models import ContactMessage

class ContactForm(forms.Form):
    '''this class is for forming a good and well formed inputs for the form.'''
    name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder':'Your name'}), label="Your name")
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder':'Your email address'}), label="Your email address")
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder':'Your message'}), label="Your message" )

    

class TicketOrderForm(forms.Form):
    LOCATIONS = [
        ('', 'Select a location...'),
        ('Cambodia', 'Cambodia'),
        ('Hong Kong', 'Hong Kong'),
        ('India', 'India'),
        ('Japan', 'Japan'),
        ('Korea', 'Korea'),
        ('Laos', 'Laos'),
        ('Myanmar', 'Myanmar'),
        ('Singapore', 'Singapore'),
        ('Thailand', 'Thailand'),
        ('Vietnam', 'Vietnam'),
    ]
    CHOICES = [('round', 'Round'), ('one-way', 'Oneway')]

    from_location = forms.ChoiceField(choices=LOCATIONS, required=True, label='From')
    to_location = forms.ChoiceField(choices=LOCATIONS, required=True, label='To')
    departure_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control date'}), required=True, label='Departure date')
    return_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control date'}), required=True, label='Return date')
    trip_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True, label='Trip Type')
    
