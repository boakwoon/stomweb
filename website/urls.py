from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('price.html', views.price, name="price"),
	path('service.html', views.service, name="service"),
	path('appointment.html', views.appointment, name="appointment"),
	path('fillings.html', views.fillings, name="fillings"),
	path('signup.html', views.signup, name="signup"),
	path('forms.html', views.forms, name="forms"),
	path('upload', views.upload, name="upload"),
	path('shop.html', views.shop, name="shop"),
	path('shop.html', views.shop, name="shop"),
	path('enroll', views.enroll, name="enroll" ),
	path('unenroll', views.unenroll, name="unenroll"),
]