from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages


from .forms import UserRegisterationForm,LoginForm
# Create your views here.

def register(request):

	if request.method == 'POST':
		form = UserRegisterationForm(data = request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = User.objects.create_user(username,email,password)
			login(request,user)
			return HttpResponseRedirect('/')

	form = UserRegisterationForm()
	dataset = dict()
	dataset['form'] = form
	return render(request,'account/register.html',dataset)



def login_view(request):
	if request.method == 'POST':
		   username = request.POST['username']
		   password = request.POST['password']
		   user = authenticate(request,username = username,password = password)
		   if user is None:
		   	return redirect('/')
		   else:
		   	login(request,user)
		   	print(request.user)
		   	return redirect(reverse('account:login'))

	form = LoginForm()
	return render(request,'account/login.html',{'form':form})