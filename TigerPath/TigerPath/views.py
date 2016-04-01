from django.shortcuts import render

from .models import Student, Course, StudentCourse

#def degree_progress(request, s_id, major_id):


# 
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