from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

# need functions to add outside course and to add princeton approved course

def compare_lists(l1, l2):
	count = 0
	for i in range(0, len(l1)):
		for j in range(0, len(l2)):
			if (i == j):
				count+=1
	return count

#have an object for each certificate, have an array of names of areas (for buttons for front end)
class COS_BSE(models.Model):
	major_name="Computer Science B.S.E."
	course_id = models.CharField(max_length = 30, primary_key=True)
	theory = models.IntegerField()
	applications = models.IntegerField()
	systems = models.IntegerField()
	core = models.IntegerField()
	other = models.IntegerField()
	iw = models.IntegerField()

	def __str__(self):
		return str(self.course_id)


class Course(models.Model):
	course_id = models.CharField(max_length = 30, primary_key = True)
	listings = models.CharField(max_length = 30)
	#courseid = models.CharField(max_length = 30, primary_key = True)
	title = models.CharField(max_length = 30)
	area = models.CharField(max_length = 30)
	S15 = models.IntegerField()
	F15 = models.IntegerField()
	S16 = models.IntegerField()
	F16 = models.IntegerField()
	description = models.CharField(max_length = 30)

	def __str__(self):
		return self.listings


# need to check if authenticated user is already in student database at some point (amybe when they're on that page where they select the major)
class Student(models.Model):
	'''Object which is unique to each student user.'''
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	student_id = models.CharField(max_length = 20, primary_key = True) #NOT SECURE < will probably need to get from CASS login!
	student_major = models.CharField(max_length = 30) # the student's major
	#student_sub_conc = models.CharField(max_length = 30) # the student's concentration within a major (relevant for ELE and MAE and others)
	courses = models.ManyToManyField(Course, through='Entry')
	cert1=models.CharField(max_length = 30)
	cert2=models.CharField(max_length = 30)
	cert3=models.CharField(max_length = 30)
	cert4=models.CharField(max_length = 30)
	cert5=models.CharField(max_length = 30)

	def __str__(self):
		return self.student_id

	def add_course(self, course, student, sem):
		# put student ID and course ID into student-course DB
		s = student
		c = course
		if Entry.objects.filter(student=student, semester=sem, course=course).exists():
			return;
		e = Entry(student=s, course=c, semester=sem)
		e.save()
	def remove_course(self, course, student, sem):
		s = student
		c = Course.objects.filter(listings=course);
		obj = Entry.objects.filter(student=s, semester=sem, course=c)
		obj.delete()


# Relevant when they are "adding" a course to their four year plan
class Entry(models.Model):
	#id = models.AutoField(primary_key = True) # we need to update the db first
	id = models.AutoField(primary_key=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	semester = models.CharField(max_length=30)#, primary_key = True)
	#requirement_list = models.CharField(max_length=30) # we need to know which requirement list its in

#for classes that were approved for major or certificate
class Approved_Course(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE) # will be something from our courses list
	semester = models.CharField(max_length=30, primary_key = True)
	requirement = models.CharField(max_length=30) # Theory, Technology and Society IT Track, etc.
	major = models.CharField(max_length=30) #COS_BSE or COS_AB
	certificate = models.CharField(max_length=30) #GSS or EAS or another certificate code


# if you did Princeton in Beijing or something (summer course, global sem, study abroad)..courses from other univiersitites
# can you use one course to count as, lets say Theory for COS and also tech and society? Maybe need two requirement parameters?
class Outside_Course(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course_name=models.CharField(max_length=30, primary_key = True)
	requirement = models.CharField(max_length=30) # Theory, Systems, Technology and Society IT Track, etc.
	major = models.CharField(max_length=30) #COS_BSE or COS_AB
	certificate = models.CharField(max_length=30) #GSS or EAS or another certificate code
	distribution = models.CharField(max_length=30) #LA or SA or something

	#def select_major():

	#WILLIAM ADDED
	# def add_course(Course, semester):
	# 	self.student_courses.add(course)
	# 	self.save()

	# def drop_course(course, semester):
	# 	self.student_courses.remove(course)

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
