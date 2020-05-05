from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from mysqlapp.forms import *
from mysqlapp.models import *
from django.core.mail import send_mail
from mysqlproject import settings
# Create your views here.	

def upload(request):
	if request.method=='POST':
		form=UserForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			sub='hi'
			body='i am coming from django app'
			receiver=request.POST['mailid']
			sender=settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			return HttpResponse('Image Uploaded.....')
	form=UserForm()
	return render(request,'mysqlapp/upload.html',{'form':form})
def display(request):
	data=Userimages.objects.all()
	return render(request,'mysqlapp/display.html',{'data':data})

