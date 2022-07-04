from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']


		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from
			['kimgrishulya@gmail.com'], # to
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def price(request):
	return render(request, 'price.html', {})

def service(request):
	return render(request, 'service.html', {})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']


		appointment = "Name: " + your_name  + " Email: " + your_email + " Schedule: " + your_schedule + " Day: " + your_date 

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			['kimgrishulya@gmail.com'], # To Email
			)
		
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_email': your_email,
			'your_schedule': your_schedule,
			'your_date': your_date
			})

	else:
		return render(request, 'home.html', {})


def fillings(request):
	return render(request, 'fillings.html', {})

def signup(request):
	return render(request, 'signup.html', {})

def forms(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_tel = request.POST['message-tel']


		# send an email
		send_mail(
			message_name, # subject
			message_tel, # message
			message_email, # from
			['kimgrishulya@gmail.com'], # to
			)

		return render(request, 'forms.html', {'message_name': message_name})

	else:
		return render(request, 'forms.html', {})

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')

def shop(request):
	return render(request, 'shop.html', {})

def enroll(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			messages.warning(request, 'Your email already exists in our database', "alert alert-warning alert-dissmissible")
		else:
			instance.save()
			messages.success(request, 'Your email has been submitted to our database', "alert alert-success alert-dissmissible")

	context = {
		'form': form,
	}
	template = "enroll.html"
	return render(request, template, context)

def unenroll(request):
	form = NewsletterUserSignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		if NewsletterUser.objects.filter(email=instance.email).exists():
			NewsletterUser.objects.filter(email=instance.email).delete()
			messages.success(request, 'Your email has been removed', "alert alert-success alert-dissmissible")
		else:
			messages.warning(request, 'Your email is not in the database', "alert alert-warning alert-dissmissible")

	context = {
		"form": form,
	}
	template = "unenroll.html"
	return render(request, template, context)
