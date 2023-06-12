from django.shortcuts import render, redirect
from contact.models import Contact, ContactTitle, ContactBody, ContactComplite
from contact.form import ContactForm

# Create your views here.

def contact(request):
    contact_title = ContactTitle.objects.all()
    contact_body = ContactBody.objects.all()

    form = ContactForm()
    massage = ''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        mes = request.POST['message']

        if len(name) < 4:
            massage = "Your username is too short"
        elif Contact.objects.filter(name=name):
            massage ='Information has already been received from this user' 
        elif Contact.objects.filter(email=email):
            massage ='Information has already been received from this email' 
        elif len(email)< 6:
            massage = "Please enter true email address"  
        else:
        
            user = Contact(name=name,email=email,subject=subject,message=mes)
            user.save()
            return redirect('contact_form')

    context = {
        'contact_title': contact_title,
        'contact_body': contact_body,
        'massage': massage
    }
    return render(request, 'co/contact.html', context)

def contact_form(request):
    contact_complite = ContactComplite.objects.all()

    context = {
        'contact_complite': contact_complite
    }
    return render(request, 'co/contact_form.html', context)