from django.shortcuts import render, redirect
from .forms import ContactForm, TicketOrderForm

# Create your views here.
def index(request):
    # View logic
    if request.method == 'POST':
        form1 = TicketOrderForm(request.POST)
        if form1.is_valid():
            pass
    else:
        form1 = TicketOrderForm()

    return render(request, 'FlightApp/index.html', {"form1": form1})
    # return render(request, 'FlightApp/index.html', context = {})

def contact(request):
    # View logic
    if request.method == 'POST':
        form2 = ContactForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('success_view_name')
    else:
        form2 = ContactForm()
    return render(request, 'FlightApp/contact.html', {"form2": form2})
    # return render(request, 'FlightApp/contact.html', context = {})

# def contact_view(request):
#     if request.method == 'POST':
#         form2 = ContactForm(request.POST)
#         if form2.is_valid():
#             form2.save()
#             return redirect('success_view_name')
#     else:
#         form2 = ContactForm()
#     return render(request, 'FlightApp/contactForm.html', {"form2": form2})

