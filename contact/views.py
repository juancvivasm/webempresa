from django.shortcuts import render, redirect
from django.urls import reverse
# Para enviar Email
from django.core.mail import EmailMessage
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
            # Enviamos mensaje y redireccionamos:
            email = EmailMessage( 
                    'La Caffettiera: Nuevo mensaje de contacto', 
                    'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content), 
                    'no-contestar@inbox.mailtrap.io', 
                    ['juanc.vivam@gmail.com'], 
                    reply_to=[email], 
                    headers={'Message-ID': 'foo'},
                )
            try:
                    email.send()
                    return redirect(reverse('contact')+'?ok')
            except:
                    return redirect(reverse('contact')+'?fail')

    return render(request, "contact/contact.html", {'form': contact_form})
