from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


def select_major(models.Model):





class Major(models.Model):
	""" The major object is a general major with selections etc bla"""


	major_text = models.CharField(max_Length = 50)	# Text form of major i.e. Computer Science
	major_code = models.choices
	major_requirements = get_requirements()
	#etc. (feel free to change this stuff)

	def __str__(self):
		'''Text which is shown to the public'''
		return self.major_text

	def get_requirements(major_code):
		return ["WrSem", "SA"]
		#Based on major code (i.e. COS, WWS, POL, etc):
		#requirments = [] -> list of objects?
		#add gen-ed requirments (if BSE: add these classes/ dist reqs, elif AB: ...)
		#add major-specific requirments (Have list of requirments in a dictionary and return all relevent ones to the major)
		#return the requirments list?


class Student(models.Model):
	'''Object which is unique to each student user.'''
	student_first_name = models.CharField(max_length = 30)
	student_last_name = models.CharField(max_length = 30)
	student_id = models.CharField(length = 9, primary_key = True) #NOT SECURE < will probably need to get from CASS login!
	student_major = models.ForeignKey(Major, on_delete=models.CASCADE)

	def __str__(self):
		return student_first_name " " student_last_name

	def required_areas(self):
		'''returns a list of distribution and concentration specific requirements. * need
		to append certificate-specific requirements'''
		return student_major.get_requirements(student_major.major_code)
	#student_certificates = [] #How to get multiple certificates?
	#Should we consider linking in other information? i.e. rescollege, biodata, etc? or na

	def change_major(self):
		self.student_major = models.ForeignKey(Major, on_delete= models.CASCADE)