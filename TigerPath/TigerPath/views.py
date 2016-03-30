from django.shortcuts import render

from .models import Student, Course, StudentCourse

def degree_progress(request, s_id, major_id):


# 
def four_year(request, s_id):
	student_courses_list = StudentCourse.objects.filter(student_id=s_id)
	context = {'student_courses_list': student_courses_list, 'student_id': s_id}
	return render(request, 'TigerPath/four_year.html', context)