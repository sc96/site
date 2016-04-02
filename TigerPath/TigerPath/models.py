from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

# maybe this should be in student Module?
#def select_major(models.Model):

def compare_lists(l1, l2):
	count = 0
	for i in range(0, len(l1)):
		for j in range(0, len(l2)):
			if (i == j):
				count+=1
	return count

class COS_BSE(models.Model):
	major_name="Computer Science B.S.E."
	course_id = models.CharField(max_length = 30, primary_key=True)
	theory = models.IntegerField()
	applications = models.IntegerField()
	systems = models.IntegerField()
	core = models.IntegerField()

	def __str__(self):
		return self.major_name

class ELE(models.Model):
	major_name="Electrical Engineering"
	course_id = models.CharField(max_length = 30, primary_key=True)
	foundation = models.IntegerField()
	core = models.IntegerField()
	math = models.IntegerField()
	breadth = models.IntegerField()
	engineering_science = models.IntegerField()
	balance = models.IntegerField()
	design = models.IntegerField()

	def __str__(self):
		return self.major_name

class MAE(models.Model):
	major_name="Mechanical and Aerospace Engineering"
	course_id = models.CharField(max_length = 30, primary_key=True)
	intro = models.IntegerField()
	math_app = models.IntegerField()
	mech_engineer = models.IntegerField()
	aero_engineer = models.IntegerField()
	mae_engineer = models.IntegerField()
	core = models.IntegerField()

	def __str__(self):
		return self.major_name

class GEN_BSE(models.Model):
	major_name="General B.S.E. Requirements"
	course_id = models.CharField(max_length = 30, primary_key=True)
	physics = models.IntegerField()
	math = models.IntegerField()
	chem = models.IntegerField()
	computer = models.IntegerField()

	# don't need these as list, instead this will be in business logic
	# basically want to have lists of EM, EC, HA, LA, SA, Language and then add course
	# the student has taken to those
	#ec = models.IntegerField()
	#em = models.IntegerField()
	#ha = models.IntegerField()
	#la = models.IntegerField()
	#sa = models.IntegerField()
	#language = models.IntegerField()
	#writing seminar

	#gen AB and gen BSE logic would be same across majors within those fields

	def __str__(self):
		return self.major_name

class Major(models.Model):
	""" The major object is a general major with selections etc bla"""

	MAJOR_CODES = (
	('Computer Science', '00'),	
	)
	major_text = models.CharField(max_length = 50)	# Text form of major i.e. Computer Science
	major_code = models.CharField(max_length = 2, choices=MAJOR_CODES, default='Computer Science')

	def __str__(self):
		'''Text which is shown to the public'''
		return self.major_text

	#def get_requirements(code):
		# now what we want to do here, is look at SQL table that corresponds with major code, 
		# then grab all lists from that - want to return N number of lists (4 for COS?) 

		#Based on major code (i.e. COS, WWS, POL, etc):
		#requirments = [] -> list of objects?
		#add gen-ed requirments (if BSE: add these classes/ dist reqs, elif AB: ...)
		#add major-specific requirments (Have list of requirments in a dictionary and return all relevent ones to the major)
		#return the requirments list?

class Course(models.Model):
	identification = models.CharField(max_length = 30)
	listings = models.CharField(max_length = 30, primary_key = True)
	courseid = models.CharField(max_length = 30)
	title = models.CharField(max_length = 30)
	area = models.CharField(max_length = 30)
	semester = models.CharField(max_length = 30)
	year = models.CharField(max_length = 30)
	description = models.CharField(max_length = 30)

	def __str__(self):
		return self.listings

class StudentCourse(models.Model):
	student_id = models.CharField(max_length = 30, primary_key = True)
	course_id = models.CharField(max_length = 30)
	semester = models.CharField(max_length = 30)

	def __str__(self):
		return self.student_id

class Student(models.Model):
	'''Object which is unique to each student user.'''
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	student_id = models.CharField(max_length = 9, primary_key = True) #NOT SECURE < will probably need to get from CASS login!
	student_major = models.CharField(max_length = 30) # the student's major
	student_sub_conc = models.CharField(max_length = 30) # the student's concentration within a major (relevant for ELE and MAE)

	#var = "ELE" # another table or choices attribute
	# WE NEED THIS ....student_major = models.ForeignKey(COS_BSE, on_delete=models.CASCADE)
	# cos BSE
	#s = Student(first_name, last_name, student_id, student_major)
	#s.save()

	def __str__(self):
		return self.first_name 
		#" " student_last_name

	def add_course(course, student):
		# put student ID and course ID into student-course DB
		s = StudentCourse(student.student_id, course.course_id)
		s.save()

	#def courses_taken(self):
		# SELECT * 
		#FROM  `TigerPath_student` 
		#WHERE  `student_id` =1
		#LIMIT 0 , 30

	#def required_areas(self):
		#'''returns a list of distribution and concentration specific requirements. * need
		#to append certificate-specific requirements'''
	#	return student_major.get_requirements(student_major.major_code)
	#student_certificates = [] #How to get multiple certificates?
	#Should we consider linking in other information? i.e. rescollege, biodata, etc? or na

#	def change_major(self):
	#	self.student_major = models.ForeignKey(Major, on_delete= models.CASCADE)

#	def get_classes(self):
		# want to return a list of all of the classes the student has stored in their four year plan
	#	return self.student_id.( #.....
