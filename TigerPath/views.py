from django.shortcuts import render
from .models import Student, Course, COS_BSE, Entry
from django.contrib.auth.decorators import login_required

@login_required # Cas authentication for this url.
def degree_progress(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	student_major = student.student_major
	# something to think about: COS 340 can't pop up in "Other" and in "Theory"
	if (student_major=="COS_BSE"):
		theory_courses = COS_BSE.objects.filter(theory="1")
		systems_courses = COS_BSE.objects.filter(systems="1")
		apps_courses = COS_BSE.objects.filter(applications="1")
		core_courses = COS_BSE.objects.filter(core="1")
		other_courses = COS_BSE.objects.filter(other="1")
		iw_courses = COS_BSE.objects.filter(iw="1")
		#context = {''}
		#return render(request, 'TigerPath/degree_progress_cos_bse.html', context)
 
@login_required # Cas authentication for this url.
def four_year(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)

	# getting list of courses for each semester
	fresh_fall = Entry.objects.filter(student_id=current_user.username, semester="FRF")
	fresh_spring = Entry.objects.filter(student_id=current_user.username, semester="FRS")
	soph_fall = Entry.objects.filter(student_id=current_user.username, semester="SOF")
	soph_spring = Entry.objects.filter(student_id=current_user.username, semester="SOS")
	junior_fall = Entry.objects.filter(student_id=current_user.username, semester="JRF")
	junior_spring = Entry.objects.filter(student_id=current_user.username, semester="JRS")
	senior_fall = Entry.objects.filter(student_id=current_user.username, semester="SRF")
	senior_spring = Entry.objects.filter(student_id=current_user.username, semester="SRS")
	context = {'user': current_user.username,'fresh_fall': fresh_fall, 'fresh_spring': fresh_spring, 
	'soph_fall': soph_fall, 'soph_spring': soph_spring, 'junior_fall': junior_fall, 'junior_spring': junior_spring,
	'senior_fall': senior_fall, 'senior_spring': senior_spring}
	return render(request, 'TigerPath/four_year.html', context)

# Natalie's code for displaying BSE requirements for all BSE students
# not added to either view yet though, so not sure if it works
ec_requirements = Course.objects.filter(area='EC')
em_requirements = Course.objects.filter(area='EM')
la_requirements = Course.objects.filter(area='LA')
sa_requirements = Course.objects.filter(area='SA')
ha_requirements = Course.objects.filter(area='HA')
writing_sem = Course.objects.filter(listings__regex='WRI1')
foreign_lang = Course.objects.filter(listings__regex='(ARA|BCS|CHI|CZE|FRE|GER|HEB|HIN|ITA|JPN|KOR|LAT|POL|POR|RUS|SPA|SWA|TUR|TWI|URD)')




##Will's new four_year file based on ManyToManyField representation
# def four_year(request, s_id):
#"""Filters data for presentation. NOT CHECKED YET (I still can't use MySQL) """
	# fresh_fall=[]
	# fresh_spring=[]
	# soph_fall=[]
	# soph_spring=[]
	# junior_fall=[]
	# junior_spring=[]
	# senior_fall=[]
	# senior_spring=[]
	# student_courses_list = StudentCourse.objects.filter(student_id=s_id)
	# student = Student.objects.filter(student_id=s_id)
	# name = student[0].first_name + " " + student[0].last_name
	# courses_list = Course.objects.all()
	# for s in student.student_courses:
		#if (s.course_id == c.identification):
	# 		if (s.semester=="FRF"):
	# 				fresh_fall.append(c)
	# 			elif(s.semester=="FRS"):
	# 				fresh_spring.append(c)
	# 			elif(s.semester=="SOF"):
	# 				soph_fall.append(c)
	# 			elif(s.semester=="SOS"):
	# 				soph_spring.append(c)
	# 			elif(s.semester=="JRF"):
	# 				junior_fall.append(c)
	# 			elif(s.semester=="JRS"):
	# 				junior_spring.append(c)
	# 			elif(s.semester=="SRF"):
	# 				senior_fall.append(c)
	# 			elif(s.semester=="SRS"):
	# 				senior_spring.append(c)
	# context = {'student_courses_list': student_courses_list,'student_id': s_id, 'student': student,
	# 'fresh_fall': fresh_fall, 'fresh_spring': fresh_spring, 'soph_fall': soph_fall, 'soph_spring': soph_spring,
	# 'junior_fall': junior_fall, 'junior_spring': junior_spring, 'senior_fall': senior_fall, 'senior_spring': senior_spring}
	# return render(request, 'TigerPath/four_year.html', context)