# /StudX_dir/StudX/configuration/models.py

# System imports
import uuid

# Django imports
from django.db import models
from django.conf import settings
from datetime import datetime, date, time, timedelta
from django.utils.translation import gettext as _ # for internationalization
from django.utils import timezone
from django.contrib.auth.models import User

# Apps imports
from common.utils import *

'''
A "classe" is a group of a given number of student (e.g. max. 25 student per classe) having the same set of subjects.
A classe can have as little as a single student and a maximum number of student decided by the school authority. Classes may share subjects taught by the same teacher. 
Therefore, if the number of student assigned to the same set of subjects outnumbered the maximum per classe, a new one is created and eventually the total number of student is equally distributated between the classes.
'''
class Classes(models.Model):
	__tablename__ = 'Classes'
	
	classe_name = models.CharField(_('classe'), max_length=45, null=True, blank=True)
	formation = models.ForeignKey('Formation', on_delete=models.CASCADE, related_name='classes', null=True, blank=True)
	subject = models.ManyToManyField(to='Subjects', related_name='classe_subjects', through='SubjectsSet', blank=True)
	is_active = models.BooleanField(default=True)
	max_students = models.IntegerField(_('Capacité maximum'), default=25)
	start_date = models.DateField(_('Date de début'), null=True, blank=True)
	end_date = models.DateField(_('Date de fin'), null=True, blank=True)
	
	def __str__(self):
		return '{}'.format(self.classe_name)
	
	def get_student_count(self):
		return self.student_classe.count()
	
	def get_available_spots(self):
		return self.max_students - self.get_student_count()
	
	class Meta:
		verbose_name = _("Classe")
		verbose_name_plural = _("Classes")		

'''
Classroom
'''		
class Location(models.Model):
	__tablename__='Location'
		
	location = models.CharField(max_length=25, unique=True)
	capacity = models.SmallIntegerField(null=True, blank=True)
	
	def __str__(self):
		return '{}'.format(self.location)	

class SubjectsSet(models.Model):
	__tablename__='SubjectsSet'
	
	subject = models.ForeignKey(to='Subjects', on_delete=models.CASCADE, related_name='+')
	classe = models.ForeignKey(to='Classes', on_delete=models.CASCADE, related_name='+')
	hours = models.IntegerField(null=True, blank=True)
	set = models.CharField(max_length=10, blank=True)	
	
	def __str__(self):
		return '{} - {} - {}'.format(self.subject, self.classe, self.set)	
	
	
class Subjects(models.Model):
	__tablename__='Subjects'
	
	code = models.CharField(max_length=20, unique=True)
	name = models.CharField(max_length=50, blank=True)
	description = models.CharField(max_length=255, null=True, blank=True) # Free text
	
	def __str__(self):
		return '{} - {}'.format(self.code, self.name)	
	
	class Meta:
		verbose_name = _('Subject')
		verbose_name_plural = _('Subjects')
		
class Formation(models.Model):
	"""
	Une formation est un programme d'études complet (ex: Développement Web, Marketing Digital)
	Une formation peut avoir plusieurs classes (groupes d'étudiants)
	"""
	__tablename__ = 'Formation'
	
	name = models.CharField(_('Nom de la formation'), max_length=100)
	description = models.TextField(_('Description'), blank=True)
	duration_months = models.IntegerField(_('Durée en mois'), default=6)
	price = models.DecimalField(_('Prix'), max_digits=10, decimal_places=2, default=0)
	max_students_per_class = models.IntegerField(_('Capacité par classe'), default=25)
	is_active = models.BooleanField(_('Active'), default=True)
	subjects = models.ManyToManyField('Subjects', related_name='formations', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.name
	
	def get_total_students(self):
		return sum(classe.student_classe.count() for classe in self.classes.all())
	
	def get_completion_rate(self):
		return 85
	
	class Meta:
		verbose_name = _('Formation')
		verbose_name_plural = _('Formations')
		ordering = ['name']
	
