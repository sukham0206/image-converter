from django.shortcuts import render
from home.models import Form
from home.modules import converter
from django.core.mail import EmailMessage


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        size = request.POST.get('size')
        email = request.POST.get('email')
        file = request.FILES.get('file')
        index = Form(name= name, size= size, email = email, file = file)
        index.save()
        converter.convert(index.file.path, size)
        
        
        #email.send_email(str(request.POST.get('email')), index.file.path)
        
        send_email = EmailMessage(
        'Thank you for using this service',
        'Here is your image',
        to=[email]
        )
        send_email.attach_file(index.file.path)
        send_email.send()
        
    return render(request, 'index.html')