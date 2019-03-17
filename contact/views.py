from django.shortcuts import render, redirect
from django.urls import reverse
# Importamos el Frm
from .forms import ContactForm

# Create your views here.
def contact(request):
    # print("Tipo de peticion: {}".format(request.method))
    contact_form = ContactForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        contact_form = ContactForm(data=request.POST)
        # check whether it's valid:
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # redirect suponiendo que todo esta bien:
            return redirect(reverse('contact')+'?ok')

    return render(request, "contact/contact.html", {'form': contact_form})
