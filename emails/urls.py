from django.urls import path
from . import views

urlpatterns = [
	path('email-invoice/', views.email_invoice, name='email-invoice'),
]