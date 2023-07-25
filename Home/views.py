from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def index(request):
    #return HttpResponse("this is home page.") 
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
         #messages.success(request, 'Your message has been sent !')
    return render(request, 'index.html')
