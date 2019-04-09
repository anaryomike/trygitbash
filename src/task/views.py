from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
import datetime

# Create your views here.

from .models import Task
from .forms import CreateTask


def task_list(request):
	queryset= Task.objects.all()
	query = request.GET.get('query')
	print(query in request.GET)
	if query:

		queryset = queryset.filter(
		Q(name__icontains=query) |
		Q(priority__icontains=query) |
		Q(status__icontains=query) 

	)

	dataset = {
	'tasks':queryset,
	'title':'Task Here'
	}


	template = 'task/tasks.html'

	return render(request,template,dataset)


# @login_required
def create_task(request):
	dataset = dict()
	if not request.user.is_authenticated:
		return HttpResponse('user not registered')

	if request.method == 'POST':
		# if 'save' in request.POST:
		# 	print("save")
		# if 'save & new' in request.POST:
		# 	return HttpResponseRedirect('/')
		form = CreateTask(request.POST)
		if form.is_valid():

			template = 'task/tasks.html'

			title = 'Tasks'

			instance = form.save(commit = False)
			instance.owner = request.user
			instance.save()
			tasks = Task.objects.all()
		
			dataset['tasks'] = tasks
			dataset['title'] = title
		

			return render(request,template,dataset)

	dataset['form'] = CreateTask()
	template = 'task/create_task.html'
	return render(request,template,dataset)




def delete_task(request,task_id):
	task = get_object_or_404(Task, id = task_id)
	task.delete()
	dataset = dict()
	dataset['tasks'] = Task.objects.all()
	dataset['title'] = 'Task'
	template = 'task/tasks.html'
	return render(request,template,dataset)


def edit_task(request,task_id):
	dataset = dict()
	task = get_object_or_404(Task, id = task_id)
	print(task.updated)
	if request.method == 'POST':
		form = CreateTask(data = request.POST, instance = task)
		instance = form.save(commit=False)
		instance.status = 'approve'
		instance.save()
		print(task.updated)

		
		return render(request,'task/tasks.html',{'tasks':Task.objects.all()})

	form = CreateTask(instance = task)
	return render(request,'task/create_task.html',{'form':form})




def detail_task(request,id):
	task = get_object_or_404(Task,id = id)
	return render(request,'task/detail.html',{'task':task})




def task_done(request,task_id):
	task = get_object_or_404(Task, id = task_id)
	# print(task.completed_task)
	task.completed_task
	return redirect('/')
	return HttpResponse(task_id)





# Approve and Pending
def approve(request,id):
	task = get_object_or_404(Task,id = id)
	task.status = 'approve'
	task.save()
	return render(request,'task/detail.html',{'task':task})




def delete_all_approved(request):
	queryset = Task.objects.filter(end=datetime.date.today())
	print(queryset,queryset.count())
	return HttpResponse('working')



def march_reminder(request):
	today = datetime.date.today()

	m = today.month
	y = today.year

	tasks = Task.objects.filter(end__month=m,end__year=y)
	print(tasks)

	c = {'tasks':tasks}

	return render(request,'task/reminder.html',c)
