from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviar correo y redireccionar
            email_message = EmailMessage(
                "reseñaslibros: Nuevo Mensaje de Contacto",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "noreply@reseñaslibros.test",
                ["test@test.com"],
                reply_to=[email]
            )
            try:
                email_message.send()
                return redirect(reverse('contact') + '?ok')
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {
        'form': contact_form
    })
