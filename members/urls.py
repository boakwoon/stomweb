from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
]

# Admin Titles
admin.site.site_header = "DentCare Administration Panel"