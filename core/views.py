from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

@login_required
def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')