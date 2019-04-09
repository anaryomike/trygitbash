from django.utils.translation import ugettext_lazy as _
from django import forms 
from .models import Task
import datetime


class CreateTask(forms.ModelForm):

	description = forms.CharField(label='describe your task',
	widget = forms.Textarea(
		attrs={
		'row':250
		}
	)

	)

	priority = forms.CharField(label='Task Priority Rate (Default : High)',widget=forms.RadioSelect(choices=Task.PRIORITY),help_text=_("how important the Task is to you"))
	class Meta:
		model = Task
		fields = ['name','description','start','end','priority']


	def clean_end(self):
		end_date = self.cleaned_data['end']
		start_date = self.cleaned_data['start']

		if end_date < datetime.date.today():
			print('enddate in the past')
		elif end_date == start_date:
			print('both dates are today')
		elif start_date < datetime.date.today():
			print('start date in the past')
			
		return end_date

	def clean_name(self):
		name = self.cleaned_data['name']
		qry = Task.objects.filter(name = name)
		if qry.exists():
			print("Task with same name exist")
		return name


