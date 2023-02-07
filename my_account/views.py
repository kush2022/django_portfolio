from django.shortcuts import render, redirect 

from django.contrib import messages
from . forms import ContactForm, MessageForm
from . models import Blog

from django.core.mail import send_mail

# Create your views here.

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['description']
            
            send_mail(
                subject + " from " + name,
                message,
                email,
                ['felixkuria12@gmail.com'],
                fail_silently=False
            )
            messages.info(request, 'The message has been sent. I will get back to you.')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form
    }    
    return render(request, 'my_account/contact.html', context)


def blog(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'my_account/blog.html', context)


def testimonials(request):
    return render(request, 'my_account/testimonials.html')


def message_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message been sent. Thank you ):')
        else:
            messages.error(request, 'Something went wrong while sending the message. Please send again...')
    
    form = MessageForm()

    context = {
        'form': form 
    }

    return render(request, 'my_account/msg.html', context)