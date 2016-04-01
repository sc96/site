from django.shortcuts import render

from .models import Student, Course, StudentCourse, COS_BSE

def degree_progress(request, s_id, major_id):
	theory_on=[]
	theory_off=[]
	systems_on=[]
	systems_off=[]
	apps_on=[]
	apps_off=[]
	core_on=[]
	core_off=[]
	student_courses_list = StudentCourse.objects.filter(student_id=s_id)
	name = Student.objects.filter(student_id=s_id)
	student = name[0].first_name + " " + name[0].last_name
	#if (major_id == 0):
	theory_courses = COS_BSE.objects.filter(theory="1")
	systems_courses = COS_BSE.objects.filter(systems="1")
	apps_courses = COS_BSE.objects.filter(applications="1")
	core_courses = COS_BSE.objects.filter(core="1")
	for s in student_courses_list:
		for c in theory_courses:
			if (s.course_id == c.course_id):
				theory_on.append(c) 
			elif(c not in theory_off):
				theory_off.append(c)
	for s in student_courses_list:
		for c in systems_courses:
			if (s.course_id == c.course_id):
				systems_on.append(c) 
			elif(c not in systems_off):
				systems_off.append(c)
	for s in student_courses_list:
		for c in apps_courses:
			if (s.course_id == c.course_id):
				apps_on.append(c) 
			elif(c not in apps_off):
				apps_off.append(c)
	for s in student_courses_list:
		for c in core_courses:
			if (s.course_id == c.course_id):
				core_on.append(c) 
			elif(c not in core_off):
				core_off.append(c)
	context = {'theory_on': theory_on, 'theory_off': theory_off, 'apps_on': apps_on,
		'apps_off': apps_off, 'systems_off': systems_off, 'systems_on': systems_on,
	 	'core_on': core_on, 'core_off': core_off, 'student': student}
	return render(request, 'TigerPath/degree_progress_cos_bse.html', context)
 
def four_year(request, s_id):
	c_names=[]
	student_courses_list = StudentCourse.objects.filter(student_id=s_id)
	name = Student.objects.filter(student_id=s_id)
	student = name[0].first_name + " " + name[0].last_name
	courses_list = Course.objects.all()
	for s in student_courses_list:
		for c in courses_list:
			if (s.course_id == c.identification):
				c_names.append(c) 
	context = {'student_courses_list': student_courses_list,'student_id': s_id, 'c_names': c_names, 'student': student}
	return render(request, 'TigerPath/four_year.html', context)


##Will's new four_year file based on ManyToManyField representation
# def four_year(request, s_id):
"""Filters data for presentation. NOT CHECKED YET (I still can't use MySQL) """
	# c_names=[]
	# student_courses_list = StudentCourse.objects.filter(student_id=s_id)
	# individual = Student.objects.filter(student_id=s_id)
	# student = individual[0].first_name + " " + individual[0].last_name
	# courses_list = Course.objects.all()
	# for s in individual.student_courses:
	# 	c_names.append(c) 
	# context = {'student_courses_list': student_courses_list,'student_id': s_id, 'c_names': c_names, 'student': student}
	# return render(request, 'TigerPath/four_year.html', context)