from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):

	firstname = models.CharField(max_length=125)
	lastname = models.CharField(max_length=125)
	dept = models.ForeignKey('Department',on_delete = models.SET_NULL,null=True,default=1)
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(blank=True, null=True)

	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['-firstname','-dept']


	def __str__(self):
		return self.firstname



	def soft_delete(self):
		self.is_deleted = True
		self.deleted_at = timezone.now()
		self.save()




	def undo_delete(self):
		self.is_deleted = False
		self.deleted_at = timezone.now()
		self.save()





class Department(models.Model):
	name = models.CharField(max_length=20)


	def __str__(self):
		return ('{0}'.format(self.name))


	def employees_in_department(self):
		queryset = Employee.objects.filter(dept__name = self.name)
		if queryset:
			return queryset
		return None


	def total_employees_in_department(self):
		count = 0
		queryset = Employee.objects.filter(dept__name = self.name)
		if queryset:
			count = queryset.count()
			return count
		return count







