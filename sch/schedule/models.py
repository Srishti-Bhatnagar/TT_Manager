from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, UserManager, Group


class Subject(models.Model):
	"""docstring or Subject"""
	
	subject_code=models.IntegerField(blank=False,default=0)
	subject=models.CharField(max_length=5,default="",primary_key=True)

	def __str__(self):
		return self.subject

	class Meta:
		ordering = ('subject_code',)
	#def ret_code(self):
	#	return self.subject_code
	


class Schedule(models.Model):
	Sid=models.CharField(max_length=3,primary_key=True)
	day = models.CharField(max_length=9,default="")
	slots = models.CharField(max_length=8,default="")
	subject= models.ForeignKey(Subject,default="")

	def __str__(self):
		return self.Sid

	def ret_sub(self):
		return self.subject

	class Meta:
		ordering = ('Sid',)


class Teacher(models.Model):
	Tid =models.CharField(max_length=6,primary_key=True)
	TT = models.ManyToManyField(Schedule)
	password = models.CharField(max_length=10,default="")
	name= models.CharField(max_length=20,default="")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('Tid',)


class Batch(models.Model):
	sem=models.CharField(max_length=1,default="")
	stream=models.CharField(max_length=3,default="")	
	year = models.IntegerField(blank=False,default=0)
	TT = models.ManyToManyField(Schedule)
	teachers = models.ManyToManyField(Teacher)

	
	def __str__(self):
		return str(self.stream)

	class Meta:
		ordering = ('year',)







