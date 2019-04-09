from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.

class Task(models.Model):
	LOW = 'low'
	MEDIUM = 'medium'
	HIGH = 'High'


	PRIORITY = (
	(LOW,'Low'),
	(MEDIUM,'Medium'),
	(HIGH,'High'),

	)

	owner = models.ForeignKey(User,on_delete = models.CASCADE, default = 1)
	name = models.CharField(max_length=125, blank=False,null=False)
	description = models.CharField(max_length=225,blank=False,null=False)
	priority = models.CharField(max_length=7,choices=PRIORITY,default=HIGH)

	completed = models.BooleanField(default=False)
	cancelled = models.BooleanField(default=False)

	start = models.DateField(blank=False,null=False)
	end   = models.DateField(blank=False,null=False)

# Appending and accepted example
	status = models.CharField(max_length=8,default="pending")

	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)



	class Meta:
		ordering = ['-created','-updated']



	def __str__(self):
		
		return ('{0} - {1}'.format(self.name,self.description[:25]))




	@property
	def is_due(self):
		'''
		return False if task end date is in the future else True
		ie. task.end > date  for today (tomorrow > today : TRUE)
		'''
		if self.end > datetime.date.today():
			return False
		return True



	@property
	def task_lapse_today(self):
		return self.end == datetime.date.today()



	@property
	def cancel_task(self):
		'''
		If not True ie. if its False
		'''
		if not self.cancelled:
			self.cancelled = True
			self.save()


	@property
	def uncancel_task(self):
		if self.cancelled:
			self.cancelled = False
			self.save()



	@property
	def completed_task(self):
		if not self.completed:
			self.completed = True
			self.save()


	@property
	def uncomplete_task(self):
		if self.completed:
			self.completed = False
			self.save()


	@property
	def task_days_count(self):
		days = ''
		today_date = datetime.date.today()
		due_date = self.end

		if not self.is_due:
			days = (due_date - today_date).days
			return days
		days = (today_date - due_date).days
		return days



	@property
	def task_expired_today(self):
		today = datetime.date.today()
		due_date = self.end

		if today == due_date:
			return True
		return False


	@property
	def check_approve(self):
		status = False
		if self.status == 'pending':
			return status
		else:
			status = True
		return status



	

	

