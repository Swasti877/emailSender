from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'customer/index.html')

def email_info(request):
    myto = request.POST['to']
    mySubject = request.POST['subject']
    mymessage = request.POST['message']

    #email
    send_mail(mySubject, mymessage, settings.EMAIL_HOST_USER, [myto], fail_silently=False)
    return redirect('/customer/email/')