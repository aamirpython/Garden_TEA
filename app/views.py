from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from app.models import Garden

# Create your views here.

def about(request):
    return render (request,'id/about.html')    

def contact(request):
    return render (request,'id/contact.html')

def home(request):
    return render (request,'id/home.html')  

def thanks(request):
    return render (request,'id/thanks.html')   


def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        Email_name = request.POST['email']
        subject_name= request.POST['subject']
        message = request.POST['message']

        if Garden.objects.filter(Email_name=Email_name).exists():
            messages.error(request,"Email already exists")
            return redirect('/contact/')

       
        else:
            Garden.objects.create(name=name,
                                    Email_name=Email_name,subject_name=subject_name,message=message)
            return redirect('/thanks/')




        