from django.shortcuts import render
from django.contrib.auth import authenticate , get_user_model , login , logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404,redirect



# Create your views here.

from .forms import SignUpForm

def login_view(request):
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_date.get("username")
		password = form.cleaned_date.get("password")

	context = {

	 "form" : form
	 } 

	return render(request , "login.html " , context)

def register_view(request):
	return render(request , "  " , {})	

def logout_view(request):
	return render(request , "  " , {})	


def signup(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')

	else:
		form=SignUpForm()
		
		context={
		"form" : form
		}		

	return render(request,'signup.html',context)