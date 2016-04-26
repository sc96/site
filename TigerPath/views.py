from django.shortcuts import render
from .models import Student, Course, COS_BSE, Entry, Approved_Course, Engineer, Outside_Course, AAS, AFS, AMS, AP_Credit
from django.contrib.auth.decorators import login_required
import re
from itertools import chain

time = {"Freshman Fall": "FRF", "Freshman Spring": "FRS",
	"Sophomore Fall": "SOF","Sophomore Spring": "SOS",
	"Junior Fall":  "JRF","Junior Spring": "JRS","Senior Fall": "SRF","Senior Spring": "SRS"}

sems = {"FRF": "Freshman Fall", "FRS": "Freshman Spring",
	"SOF": "Sophomore Fall", "SOS": "Sophomore Spring",
	"JRF": "Junior Fall","JRS": "Junior Spring","SRF": "Senior Fall","SRS": "Senior Spring"}

def title(list):
	new_list=[]
	for i in list:
		new_list.append(Course.objects.get(course_id=i).listings)
	return new_list

def top_semester(sem):
	sem_cour = Entry.objects.filter(semester=sem).values_list('course_id', flat=True)
	sem_cour = title(map(int, sem_cour))
	sem_courses=[]
	for x in sem_cour:
		if re.match(r'COS', x):
			sem_courses.append(x)
			
	sem_dict = {}
	total = len(sem_courses)
	for s in sem_courses:
		# need to put it in dict if not already in there
		if s not in sem_dict:
			sem_dict[s]=1
		# else, value ++
		else:
			sem_dict[s]+=1
	top_10=[]
	for i in range(0, 10):
		if(sem_dict.keys()):
			maximum = max(sem_dict, key=lambda i: sem_dict[i])
			top_10.append(maximum + ": " + str(int(float(sem_dict.get(maximum))/float(total)*100)) + "%")
			sem_dict.pop(maximum, None)
	return top_10
	
def top_req(num):
	if (num == 1):
		required = COS_BSE.objects.filter(theory=1).values_list('course_id', flat=True)	
	elif (num == 2):
		required = COS_BSE.objects.filter(systems=1).values_list('course_id', flat=True)
	elif (num == 3):
		required = COS_BSE.objects.filter(applications=1).values_list('course_id', flat=True)
	elif (num == 4):
		required = COS_BSE.objects.filter(other=1).values_list('course_id', flat=True)
	elif (num == 5):
		required = COS_BSE.objects.filter(core=1).values_list('course_id', flat=True)
	elif (num == 6):
		required = COS_BSE.objects.filter(iw=1).values_list('course_id', flat=True)
	else:
		required = COS_BSE.objects.filter(other = 0).values_list('course_id', flat=True)
	req_cour = Entry.objects.values_list('course_id', flat=True)
	#required = COS_BSE.objects.filter(req=1).values_list('course_id', flat=True)
	req_cour = title(map(int, req_cour))
	required = title(map(int, required))
	req_courses=[]
	
	for x in req_cour:
		if x in required:
	#	if (re.match(r'COS', x) and x in required):
			req_courses.append(x)
			
	req_dict = {}
	total = len(req_courses)
	for s in req_courses:
		# need to put it in dict if not already in there
		if s not in req_dict:
			req_dict[s]=1
		# else, value ++
		else:
			req_dict[s]+=1
	top_10=[]
	for i in range(0, 10):
		if(req_dict.keys()):
			maximum = max(req_dict, key=lambda i: req_dict[i])
			top_10.append(maximum + ": " + str(int(float(req_dict.get(maximum))/float(total)*100)) + "%")
			req_dict.pop(maximum, None)
	return top_10
	
def top_course(num):
	if (num == 1):
		required = COS_BSE.objects.filter(course_id=444).values_list('course_id', flat=True)	
		req_cour = Entry.objects.filter(course_id=444).values_list('course_id', flat=True)
		sem_cour = Entry.objects.filter(course_id=444).values_list('semester', flat=True)
	elif (num == 2):
		required = COS_BSE.objects.filter(course_id=1012).values_list('course_id', flat=True)
		req_cour = Entry.objects.filter(course_id=1012).values_list('course_id', flat=True)
		sem_cour = Entry.objects.filter(course_id=1012).values_list('semester', flat=True)
	elif (num == 3):
		required = COS_BSE.objects.filter(course_id=541).values_list('course_id', flat=True)
		req_cour = Entry.objects.filter(course_id=541).values_list('course_id', flat=True)
		sem_cour = Entry.objects.filter(course_id=541).values_list('semester', flat=True)
	elif (num == 4):
		required = COS_BSE.objects.filter(course_id=1047).values_list('course_id', flat=True)
		req_cour = Entry.objects.filter(course_id=1047).values_list('course_id', flat=True)
		sem_cour = Entry.objects.filter(course_id=1047).values_list('semester', flat=True)
	else:
		required = COS_BSE.objects.filter(course_id=000).values_list('course_id', flat=True)
		req_cour = Entry.objects.filter(course_id=000).values_list('course_id', flat=True)
		sem_cour = Entry.objects.filter(course_id=000).values_list('semester', flat=True)
	#required = COS_BSE.objects.filter(req=1).values_list('course_id', flat=True)
	#sem_cour = Entry.objects.values_list('semester', flat=True)
	req_cour = title(map(int, req_cour))
	required = title(map(int, required))
	req_courses=[]
	
	for x in req_cour:
		if x in required:
			req_courses.append(x)
			
	req_dict = {}
	total = len(req_cour)
	for s in sem_cour:
		# need to put it in dict if not already in there
		#can do dictionary thing here
		if s not in req_dict:
			req_dict[sems[s]]=1
		# else, value ++
		else:
			req_dict[sems[s]]+=1
	top_10=[]
	for i in range(0, 8):
		if(req_dict.keys()):
			maximum = max(req_dict, key=lambda i: req_dict[i])
			top_10.append(maximum + ": " + str(int(float(req_dict.get(maximum))/float(total)*100)) + "%")
			req_dict.pop(maximum, None)
	return top_10

def compare_lists(stud, cour):
	similarities=[]
	differences=[]
	for i in cour:
		if i in stud:
			similarities.append(i)
		else:
			differences.append(i)
	return {"similarities": similarities, "differences": differences}
	
def num_compare(stud, cour):
	count = 0
	for i in cour:
		if i in stud:
			count+=1
	return count




# i mean we could make a view for every certificate...but that wouldn't cover people doing two certificates...would want to show on
# same page....could be possible if we used buttons though
def home(request):
	# current_user = request.user
	# try:
 #  		s = Student.objects.get(student_id=current_user)
	# except Student.DoesNotExist:
 #  		s = Student(student_id=current_user)
 #  		s.save()
	# student = Student.objects.get(student_id=current_user.username)

	# context = {'user': current_user.username}
	return render(request, 'index.html')

@login_required # Cas authentication for this url.
def profile(request):
	current_user = request.user;

	try:
   		s = Student.objects.get(student_id=str(current_user.username)) # changed this
	except Student.DoesNotExist:
		# creating new student. default values
   		s = Student(student_id=str(current_user.username), first_name = "First", last_name = "Last", engineerBool = "1", publicBool = "1", calc_1 = "0", calc_2 = "0", calc_3 = "0", lin_alg= "0", gen_chem = "0", physics = "0", cos = "0")
   		# 1 = True. 0 = False Using string instead of Bool since there's no
   		# easy way to pass Javascript booleans to python backend
   		s.save()

	student = Student.objects.get(student_id=str(current_user.username))

	firstN = ""
	lastN = ""
	engineerBool = ""
	publicBool = ""
	calc_1 = ""
	calc_2 = ""
	calc_3 = ""
	lin_alg = ""
	cert1 = ""
	cert2 = ""
	cert3 = ""

	if request.method == "POST":
		firstN = request.POST["firstN"]
		lastN = request.POST["lastN"]
		engineerBool = request.POST["engineerBool"]
		publicBool = request.POST["publicBool"]
		cert1 = request.POST["cert1"]
		cert2 = request.POST["cert2"]
		cert3 = request.POST["cert3"]
		student.update_info(student, firstN, lastN, engineerBool, publicBool, 
			cert1, cert2, cert3)
			
    
	# getting strings for context variable
	firstN = student.first_name
	lastN = student.last_name
	engineerBool = student.engineerBool
	publicBool = student.publicBool
	cert1 = student.cert1
	cert2 = student.cert2
	cert3 = student.cert3


	calc_1 = student.calc_1
	calc_2 = student.calc_2
	calc_3 = student.calc_3
	lin_alg = student.lin_alg

	ap_dict = {"calc_1": calc_1, "calc_2": calc_2, "calc_3": calc_3, "lin_alg" : lin_alg}
	context = {'user': current_user.username, 'firstN': firstN, 'lastN': lastN,
	 'engineerBool': engineerBool, 'publicBool': publicBool, 'cert1': cert1,
	 'cert2': cert2, 'cert3': cert3, 'ap_dict': ap_dict}
	return render(request, 'profile.html', context)

	

@login_required # Cas authentication for this url.
def degree_progress(request):

	

	student_ec=[]
	student_em=[]
	student_la=[]
	student_ha=[]
	student_sa=[]
	student_wri=[]
	student_foreign=[]
	current_user = request.user
	student = Student.objects.get(student_id=str(current_user.username))
	student_major = student.student_major
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	all_entries = Entry.objects.filter(student_id=current_user.username) #all of the student's entries
	save_other = []
	#dist_courses = Entry.objects.filter(student_id=current_user.username)

	removed_class = ""
	#Check if student is adding or removing a class
	if request.method == 'POST':
		if 'remove' in request.POST:
			removed_class = request.POST['remove']
			#sem = time[semester]
			student.remove_course(removed_class, student)
			

		else:
			added_class = request.POST['listing']
			added_class = Course.objects.get(listings=added_class)
			semester = request.POST['term']
			sem = time[semester]
			student.add_course(added_class, student, sem, "N/A")

	for d in all_courses:
		course = Course.objects.get(course_id=d)
		# need to add QR/STL/STN for AB majors
		if (course.area=='SA'):
			student_sa.append(d)
		elif (course.area=='LA'):
			student_la.append(d)
		elif (course.area=='HA'):
			student_ha.append(d)
		elif (course.area=='EM'):
			student_em.append(d)
		elif (course.area=='EC'):
			student_ec.append(d)
		elif(re.match(r'WRI1', course.listings)):
			student_wri.append(d)
		elif(re.match(r'(ARA|BCS|CHI|CZE|FRE|GER|HEB|HIN|ITA|JPN|KOR|LAT|POL|POR|RUS|SPA|SWA|TUR|TWI|URD)', course.listings)):
			student_foreign.append(d)

	# something to think about: COS 340 can't pop up in "Other" and in "Theory"
	# all of the requirement lists
	# can probably combine a lot of things here into one function - maybe i want the approved courses in their own list? idk
	# COS BSE Major
	# if (student_major=="COS_BSE"):
		# BSE requirements - all
	
	# this should probably be hard coded
	math_1 = Engineer.objects.filter(math_1=1).values_list('course_id', flat=True)
	math_2 = Engineer.objects.filter(math_2=1).values_list('course_id', flat=True)
	math_3 = Engineer.objects.filter(math_3=1).values_list('course_id', flat=True)
	math_4 = Engineer.objects.filter(math_4=1).values_list('course_id', flat=True)
	physics_1 = Engineer.objects.filter(physics_1=1).values_list('course_id', flat=True)
	physics_2 = Engineer.objects.filter(physics_2=1).values_list('course_id', flat=True)
	chem_1 = Engineer.objects.filter(chem_1=1).values_list('course_id', flat=True)
	cos_1 = Engineer.objects.filter(cos_1=1).values_list('course_id', flat=True)
	
		# now I need to parse out which one they've taken it - math ON/math OFF
	if (student.calc_1 == 1 and AP_Credit.objects.filter(student_name=current_user.username, course_id="538").count() == 0):
		a = AP_Credit(student_name = current_user.username, course_id = "538")
		a.save()
	if(student.calc_2 == 1 and AP_Credit.objects.filter(student_name=current_user.username, course_id="1029").count() == 0):
		a = AP_Credit(student_name = current_user.username, course_id = "1029")
		a.save()
	if(student.calc_3 == 1 and AP_Credit.objects.filter(student_name=current_user.username, course_id="1176").count() == 0):
		a = AP_Credit(student_name = current_user.username, course_id = "1176")
		a.save()
	if (student.lin_alg == 1 and AP_Credit.objects.filter(student_name=current_user.username, course_id="1160").count() == 0):
		a = AP_Credit(student_name = current_user.username, course_id = "1160")
		a.save()
	if(student.gen_chem == 1 and AP_Credit.objects.filter(student_name=current_user.username, course_id="1354").count() == 0):
		a = AP_Credit(student_name = current_user.username, course_id = "1354")
		a.save()
	if(student.physics == 1 and AP_Credit.objects.filter(student_name=current_user.username, course_id="763").count() == 0 and AP_Credit.objects.filter(student_name=current_user.username, course_id="2016").count() == 0):
		a = AP_Credit(student_name = current_user.username, course_id = "2016")
		a.save()
		b = AP_Credit(student_name = current_user.username, course_id = "763")
		b.save()
	if(student.cos == 1 and AP_Credit.objects.filter(student_name=current_user.username, course_id="444").count() == 0):
		a = AP_Credit(student_name = current_user.username, course_id = "444")
		a.save()

		# can probably shorten this a little bit later...
	theory_courses = COS_BSE.objects.filter(theory=1).values_list('course_id', flat=True).order_by('course_id')
	systems_courses = COS_BSE.objects.filter(systems=1).values_list('course_id', flat=True).order_by('course_id')
	apps_courses = COS_BSE.objects.filter(applications=1).values_list('course_id', flat=True).order_by('course_id')
	core_courses = COS_BSE.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	other_courses = COS_BSE.objects.filter(other=1).values_list('course_id', flat=True).order_by('course_id')
	iw_courses = COS_BSE.objects.filter(iw=1).values_list('course_id', flat=True).order_by('course_id')
		
	theory_on = compare_lists(all_courses, theory_courses)["similarities"]
	for t in all_entries.filter(req="Theory").values_list('course_id', flat=True).order_by('course_id'):
		theory_on.append(t)
	while len(theory_on) > 2:
		save_other.append(theory_on.pop(0))
	theory_on = title(theory_on)
	theory_off = title(compare_lists(all_courses, theory_courses)["differences"])
		
	systems_on = compare_lists(all_courses, systems_courses)["similarities"]
	for t in all_entries.filter(req="Systems").values_list('course_id', flat=True).order_by('course_id'):
		systems_on.append(t)
	while len(systems_on) > 2:
		save_other.append(systems_on.pop(0))
	systems_on = title(systems_on)
	systems_off = title(compare_lists(all_courses, systems_courses)["differences"])

	apps_on = compare_lists(all_courses, apps_courses)["similarities"]
	for t in all_entries.filter(req="Applications").values_list('course_id', flat=True).order_by('course_id'):
		apps_on.append(t)
	while len(apps_on) > 2:
		save_other.append(apps_on.pop(0))
	apps_on = title(apps_on)
	apps_off = title(compare_lists(all_courses, apps_courses)["differences"])

		# other should have all classes in "other" that the user hasn't already taken
		# will fix this bug a little later... 4/9/2016 ....!!!!
	other_on = compare_lists(all_courses, other_courses)["similarities"]
	other_on = chain(other_on, save_other)
	for t in all_entries.filter(req="Other").values_list('course_id', flat=True).order_by('course_id'):
		other_on.append(t.course_id)
	other_on = title(other_on)
	other_off = title(compare_lists(all_courses, other_courses)["differences"])

	iw_on = compare_lists(all_courses, iw_courses)["similarities"] #iw is for BSE only
	other_iw = Approved_Course.objects.filter(student_id=current_user.username, requirement="Independent")
	for t in other_iw:
		iw_on.append(t.course_id)
	iw_on = title(iw_on)
	iw_off = title(compare_lists(all_courses, iw_courses)["differences"])

	core_on = title(compare_lists(all_courses, core_courses)["similarities"])
	core_off = title(compare_lists(all_courses, core_courses)["differences"])

		# Need to add logic for only hilighting 2 theory courses then overflowing others into "other" section
		# Maybe don't display everything...display ones that only have "other"


		# Distribution Requirements
	student_sa=title(student_sa)
	student_la=title(student_la)
	student_ha=title(student_ha)
	student_em=title(student_em)
	student_ec=title(student_ec)
	student_wri=title(student_wri)
	student_foreign=title(student_foreign)

		# Outside Courses
		# Note: should probably do Outside Courses/Approved Courses first, then add to LA/SA/Theory/etc. THEN consolidate lists 
	student_outside=[]
	outside_courses = Outside_Course.objects.filter(student_id=current_user.username) # list of the student's outside courses
	for c in outside_courses.iterator():
		student_outside.append(c.course_name)


		# AP Requirements - would affect BSE on
	student_ap=[]
	#ap_classes = AP_Credit.objects.filter(student_name=current_user.username).values_list('course_id', flat=True).order_by('course_id')
	#student_ap = title(ap_classes)
	# now you can do on/off thing here
	math_1_credit=[0000]
	math_2_credit=[0000]
	math_3_credit=[0000]
	math_4_credit=[0000]
	physics_1_credit=[0000]
	physics_2_credit=[0000]
	chem_1_credit=[0000]
	cos_1_credit=[0000]
	
	# ap credit working now
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="538").exists()):
		math_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="538").values_list('course_id', flat=True)
	math_1_on = title(compare_lists(chain(all_courses, math_1_credit), math_1)["similarities"])
	math_1_off = title(compare_lists(chain(all_courses, math_1_credit), math_1)["differences"])
	#math_1_off=[]
	
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1029").exists()):
		math_2_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1029").values_list('course_id', flat=True)
	math_2_on = title(compare_lists(map(int, chain(all_courses, math_2_credit)), math_2)["similarities"])
	math_2_off = title(compare_lists(map(int, chain(all_courses, math_2_credit)), math_2)["differences"])
	
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1176").exists()):
		math_3_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1176").values_list('course_id', flat=True)
	math_3_on = title(compare_lists(map(int, chain(all_courses, math_3_credit)), math_3)["similarities"])
	math_3_off = title(compare_lists(map(int, chain(all_courses, math_3_credit)), math_3)["differences"])
	
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1160").exists()):
		math_4_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1160").values_list('course_id', flat=True)
	math_4_on = title(compare_lists(map(int, chain(all_courses, math_4_credit)), math_4)["similarities"])
	math_4_off = title(compare_lists(map(int, chain(all_courses, math_4_credit)), math_4)["differences"])
	
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="2016").exists()):
		physics_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="2016").values_list('course_id', flat=True)
	physics_1_on = title(compare_lists(map(int, chain(all_courses, physics_1_credit)), physics_1)["similarities"])
	physics_1_off = title(compare_lists(map(int, chain(all_courses, physics_1_credit)), physics_1)["differences"])
	#physics_1_on = chain(all_courses, physics_1_credit)
	#physics_1_off = physics_1
	
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="763").exists()):
		physics_2_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="763").values_list('course_id', flat=True)
	physics_2_on = title(compare_lists(map(int, chain(all_courses, physics_2_credit)), physics_2)["similarities"])
	physics_2_off = title(compare_lists(map(int, chain(all_courses, physics_2_credit)), physics_2)["differences"])
	
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1354").exists()):
		chem_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1354").values_list('course_id', flat=True)
	chem_1_on = title(compare_lists(map(int, chain(all_courses, chem_1_credit)), chem_1)["similarities"])
	chem_1_off = title(compare_lists(map(int, chain(all_courses, chem_1_credit)), chem_1)["differences"])
	
	if (AP_Credit.objects.filter(student_name=current_user.username, course_id="444").exists()):
		cos_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="444").values_list('course_id', flat=True)
	cos_1_on = title(compare_lists(map(int, chain(all_courses, cos_1_credit)), cos_1)["similarities"])
	cos_1_off = title(compare_lists(map(int, chain(all_courses, cos_1_credit)), cos_1)["differences"])

		# could literally just pass every certificate thing to this page....but that would be really dumb and bad
		# still in the process of getting new ideas for certificates...it can def be done tho...still thinking
	context = {'theory_on': theory_on, 'theory_off': theory_off, 'systems_on': systems_on, 'systems_off': systems_off,
	'apps_on': apps_on, 'apps_off': apps_off, 'other_on': other_on, 'other_off': other_off,
	'iw_on': iw_on, 'iw_off': iw_off, 'core_on': core_on, 'core_off': core_off,
	'student_sa': student_sa, 'student_la': student_la, 'student_ha': student_ha, 'student_ec': student_ec,
	'student_em': student_em, 'student_foreign': student_foreign, 'student_wri': student_wri, 'outside_courses': student_outside,
	'math_1_on': math_1_on, 'math_1_off': math_1_off, 'math_2_on': math_2_on, 'math_2_off': math_2_off, 'math_3_on': math_3_on, 'math_3_off': math_3_off,
	'math_4_on': math_4_on, 'math_4_off': math_4_off, 'chem_1_on': chem_1_on, 'chem_1_off': chem_1_off, 'cos_1_on': cos_1_on, 'cos_1_off': cos_1_off,
	'physics_1_on': physics_1_on, 'physics_1_off': physics_1_off, 'physics_2_on': physics_2_on, 'physics_2_off': physics_2_off, 
	'student_ap': student_ap, 'removed_class': removed_class, 'math_3': math_3}#, 'cos_1': cos_1}
	return render(request, 'degree_progress_cos_bse.html', context)
	# COS AB Major	
	#elif (student_major=="COS_AB"): 

def course_search(query):
	dist = ["la", "sa", "ha", "em", "ec", "qr", "stl", "stn"]
	dep = ["AAS", "AFS", "AMS", "ANT", "AOS", "APC", "ARA", 'ARC', 'ART', 'AST', 
			'ATL', 'BCS', 'CBE', 'CEE', 'CGS', 'CHI', 'CHM', 'CHV', 'CLA', 'CLG', 
			'COM', 'COS', 'CWR', 'CZE', 'DAN', 'EAS', 'ECO', 'ECS', 'EEB', 'EGR', 
			'ELE', 'ENE', 'ENG', 'ENV', 'EPS', 'FIN', 'FRE', 'FRS', 'GEO', 'GER', 
			'GHP', 'GLS', 'GSS', 'HEB', 'HIN', 'HIS', 'HLS', 'HOS', 'HPD', 'HUM',
			 'ISC', 'ITA', 'JDS', 'JPN', 'JRN', 'KOR', 'LAO', 'LAS', 'LAT', 'LIN', 
			 'MAE', 'MAT', 'MED', 'MOD', 'MOG', 'MOL', 'MSE', 'MTD', 'MUS', 'NEX', 
			 'MTD', 'MUS', 'NES', 'NEU', 'ORF', 'PAW', 'PER', 'PHI', 'PHY', 'PLS',
			  'POL', 'POP', 'POR', 'PSY', 'QCB', 'REL', 'RES', 'RUS', 'SAN', 'SAS', 
			  'SLA', 'SML', 'SOC', 'SPA', 'STC', 'SWA', 'THR', 'TPP', 'TRA', 'TUR', 
			  'TWI', 'URB', 'URD', 'VIS', 'WRI', 'WWS']
	commonTerms = [ "and", "in", "for", "with", "to", "an", "of", "on", "from", "their", "the", "that", "i",
	"its", "it's", "is", "there", "a"]

	if len(query) == 0:
		matched_courses = Course.objects.none()
		return matched_courses

	terms = query.split()
	matched_courses = Course.objects.all()	
	for x in terms:
		if len(x) <= 0:
			continue;
		elif x in commonTerms:
			continue;
		elif x in dist:
			matched_courses = matched_courses.filter(area__icontains=x)
		elif len(x) == 3 and x.isalpha() and x.upper() in dep:
			matched_courses = matched_courses.filter(listings__icontains=x)
		elif len(x) <= 3 and x.isdigit():
			matched_courses = matched_courses.filter(listings__icontains=x)
		elif len(x) == 6 and x[3:].isdigit() and x[:3].isalpha():
			matched_courses = matched_courses.filter(listings__icontains=x)
		else:
			matched_courses = matched_courses.filter(title__icontains=x)

	return matched_courses

def add_class(student, course, semester, req):
	time = {"Freshman Fall": "FRF", "Freshman Spring": "FRS",
	"Sophomore Fall": "SOF","Sophomore Spring": "SOS",
	"Junior Fall":  "JRF","Junior Spring": "JRS","Senior Fall": "SRF","Senior Spring": "SRS"}
	course = Course.objects.get(listings=course)
	sem = time[semester]
	student.add_course(course, student, sem, req)



@login_required # Cas authentication for this url.
def four_year(request,search):
	
	current_user = request.user
	try:
   		s = Student.objects.get(student_id=current_user.username)
	except Student.DoesNotExist:
   		s = Student(student_id=str(current_user.username))
   		s.save()
	student = Student.objects.get(student_id=current_user.username)

	added_class = ""
	semester = ""
	text = ""
	removed_class = ""
	test = ""
	#Check if student is adding or removing a class
	if request.method == 'POST':
		if 'remove' in request.POST:
			removed_class = request.POST['remove']
			sem = request.POST['term']
			#sem = time[semester]
			student.remove_course(removed_class, student, sem)
			

		else:
			added_class = request.POST['listing']
			added_class = Course.objects.get(listings=added_class)
			semester = request.POST['semester']
			sem = time[semester]
			req = request.POST['COSreq']
			student.add_course(added_class, student, sem, req)
		#add_class(student, added_class, semester)
	#Return matched courses for search bar
	
	if 'q' in request.GET:
		test = request.GET["q"]
	matched_courses = course_search(test);
	
	# getting list of courses for each semester
	fresh_fall = Entry.objects.filter(student_id=current_user.username, semester="FRF")
	app_frf = Approved_Course.objects.filter(student_id=current_user.username), semester="FRF")
	all_frf = chain(fresh_fall, app_frf)
	fresh_spring = Entry.objects.filter(student_id=current_user.username), semester="FRS")
	app_frs = Approved_Course.objects.filter(student_id=current_user.username, semester="FRS")
	all_frs = chain(fresh_spring, app_frs)
	soph_fall = Entry.objects.filter(student_id=current_user.username, semester="SOF")
	app_sof = Approved_Course.objects.filter(student_id=current_user.username, semester="SOF")
	all_sof = chain(soph_fall, app_sof)
	soph_spring = Entry.objects.filter(student_id=current_user.username, semester="SOS")
	app_sos = Approved_Course.objects.filter(student_id=current_user.username, semester="SOS")
	all_sos = chain(soph_spring, app_sos)
	junior_fall = Entry.objects.filter(student_id=current_user.username, semester="JRF")
	app_jrf = Approved_Course.objects.filter(student_id=current_user.username, semester="JRF")
	all_jrf = chain(junior_fall, app_jrf)
	junior_spring = Entry.objects.filter(student_id=current_user.username, semester="JRS")
	app_jrs = Approved_Course.objects.filter(student_id=current_user.username, semester="JRS")
	all_jrs = chain(junior_spring, app_jrs)
	senior_fall = Entry.objects.filter(student_id=current_user.username, semester="SRF")
	app_srf = Approved_Course.objects.filter(student_id=current_user.username, semester="SRF")
	all_srf = chain(senior_fall, app_srf)
	senior_spring = Entry.objects.filter(student_id=current_user.username, semester="SRS")
	app_srs = Approved_Course.objects.filter(student_id=current_user.username, semester="SRS")
	all_srs = chain(senior_spring, app_srs)

	student_outside=[]
	outside_courses = Outside_Course.objects.filter(student_id=current_user.username) # list of the student's outside courses
	for c in outside_courses.iterator():
		student_outside.append(c.course_name)

	context = {'user': current_user.username,'fresh_fall': all_frf, 'fresh_spring': all_frs, 
	'soph_fall': all_sof, 'soph_spring': all_sos, 'junior_fall': all_jrf, 'junior_spring': all_jrs,
	'senior_fall': all_srf, 'senior_spring': all_srs, 'student_outside': student_outside,'test': test, 'matched_courses': matched_courses, 'test_course': added_class, 'sem': semester,
	 'removed_class': removed_class }
	return render(request, 'four_year.html', context, )


#@login_required # Cas authentication for this url.
# if you got a course at Princeton to count as a COS departmental
#def princeton_course_approval(request):
	#current_user = request.user
	#test=""
	#if request.method == 'POST':
		#added_class = request.POST['listing']
#added_class = Course.objects.get(listings=added_class)
		#semester = request.POST['semester']
		#sem = time[semester]
		#student.add_course(added_class, student, sem)
		#add_class(student, added_class, semester)
	#Return matched courses for search bar
		
	#if 'q' in request.GET:
		#test = request.GET["q"]
	#matched_courses = course_search(test);
		
	#context = {'user': current_user.username, 'matched_courses': matched_courses}
	#return render(request, 'ptonapproval.html', context)

@login_required # Cas authentication for this url.
# if you got a course at Princeton to count as a COS departmental
def outside_course_approval(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	context = {}
	return render(request, 'outapproval.html', context)
	
@login_required # Cas authentication for this url.
# if you got a course at Princeton to count as a COS departmental
def cos_data_semester(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	frf_data = top_semester("FRF")
	frs_data = top_semester("FRS")
	sof_data = top_semester("SOF")
	sos_data = top_semester("SOS")
	jrf_data = top_semester("JRF")
	jrs_data = top_semester("JRS")
	srf_data = top_semester("SRF")
	srs_data = top_semester("SRS")
	context = {'frf_data': frf_data, 'frs_data': frs_data, 'sof_data': sof_data, 'sos_data': sos_data, 'jrf_data': jrf_data,
	'jrs_data': jrs_data, 'srf_data': srf_data, 'srs_data': srs_data}
	return render(request, 'cosdatasemester.html', context)
	
@login_required # Cas authentication for this url.
# if you got a course at Princeton to count as a COS departmental
def cos_data_course(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	one_data = top_course(1)
	two_data = top_course(2)
	three_data = top_course(3)
	four_data = top_course(4)
	context = {'one_data': one_data, 'two_data': two_data, 'three_data': three_data, 'four_data': four_data}
	return render(request, 'cosdatacourse.html', context)
	
@login_required # Cas authentication for this url.
# if you got a course at Princeton to count as a COS departmental
def cos_data_req(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	theory_data = top_req(1)
	systems_data = top_req(2)
	apps_data = top_req(3)
	iw_data = top_req(6)
	core_data = top_req(5)
	other_data = top_req(4)
	context = {'theory_data': theory_data, 'systems_data': systems_data, 'apps_data': apps_data, 'iw_data': iw_data, 'core_data': core_data,
	'other_data': other_data}
	return render(request, 'cosdatareq.html', context)

@login_required # Cas authentication for this url.
def schedule_sharing(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	nStudents = Student.objects.count
	points_dict={}
	# the user's courses
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True)
	all_sems = Entry.objects.filter(student_id=current_user.username).values_list('semester', flat=True)
	for s in Student.objects.iterator():
		# if its same semester and class = +2
		# same class = +1
		nSimilarClasses=0
		# this student's classes (the student we're comparing against)
		comp_courses = Entry.objects.filter(student_id=s.student_id).values_list('course_id', flat=True)
		comp_sems = Entry.objects.filter(student_id=s.student_id).values_list('semester', flat=True)
		# can add some more stuff in terms of (if same_certificate, then +2 or something)
		for i in range(0, len(comp_courses)):
			for j in range(0, len(all_courses)):
				if (comp_courses[i]==all_courses[j] and comp_sems[i]==all_sems[j]):
					nSimilarClasses+=2
				elif (comp_courses[i]==all_courses[j]):
					nSimilarClasses+=1
		points_dict[s.student_id]=nSimilarClasses
	length = len(points_dict)
	top_5=[]
	for i in range(0, 5):
		if(points_dict.keys()):
			maximum = max(points_dict, key=lambda i: points_dict[i])
			if (Student.objects.get(student_id=maximum).publicBool):
				top_5.append(maximum)
			else:
				top_5.append("Student" + str(Student.objects.get(student_id=maximum).id))
			points_dict.pop(maximum, None)
	# then can do a generic thing for clicking on one of top 5 students and it shows you their four year

	context = {'user': current_user.username,'nStudents': nStudents, 'len': length, 'top_5': top_5}
	return render(request, 'sharing.html', context)

@login_required # Cas authentication for this url.
def share(request, shared_user):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	if (re.match(r'Student', shared_user)):
		num = shared_user[8:]
		fresh_fall = Entry.objects.filter(id=num, semester="FRF")
		app_frf = Approved_Course.objects.filter(id=num, semester="FRF")
		all_frf = chain(fresh_fall, app_frf)
		fresh_spring = Entry.objects.filter(id=num, semester="FRS")
		app_frs = Approved_Course.objects.filter(id=num, semester="FRS")
		all_frs = chain(fresh_spring, app_frs)
		soph_fall = Entry.objects.filter(id=num, semester="SOF")
		app_sof = Approved_Course.objects.filter(id=num, semester="SOF")
		all_sof = chain(soph_fall, app_sof)
		soph_spring = Entry.objects.filter(id=num, semester="SOS")
		app_sos = Approved_Course.objects.filter(id=num, semester="SOS")
		all_sos = chain(soph_spring, app_sos)
		junior_fall = Entry.objects.filter(id=num, semester="JRF")
		app_jrf = Approved_Course.objects.filter(id=num, semester="JRF")
		all_jrf = chain(junior_fall, app_jrf)
		junior_spring = Entry.objects.filter(id=num, semester="JRS")
		app_jrs = Approved_Course.objects.filter(id=num, semester="JRS")
		all_jrs = chain(junior_spring, app_jrs)
		senior_fall = Entry.objects.filter(id=num, semester="SRF")
		app_srf = Approved_Course.objects.filter(id=num, semester="SRF")
		all_srf = chain(senior_fall, app_srf)
		senior_spring = Entry.objects.filter(id=num, semester="SRS")
		app_srs = Approved_Course.objects.filter(id=num, semester="SRS")
		all_srs = chain(senior_spring, app_srs)
	else:
	#all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses - course ID
	# getting list of courses for each semester
		fresh_fall = Entry.objects.filter(student_id=shared_user, semester="FRF")
		app_frf = Approved_Course.objects.filter(student_id=shared_user, semester="FRF")
		all_frf = chain(fresh_fall, app_frf)
		fresh_spring = Entry.objects.filter(student_id=shared_user, semester="FRS")
		app_frs = Approved_Course.objects.filter(student_id=shared_user, semester="FRS")
		all_frs = chain(fresh_spring, app_frs)
		soph_fall = Entry.objects.filter(student_id=shared_user, semester="SOF")
		app_sof = Approved_Course.objects.filter(student_id=shared_user, semester="SOF")
		all_sof = chain(soph_fall, app_sof)
		soph_spring = Entry.objects.filter(student_id=shared_user, semester="SOS")
		app_sos = Approved_Course.objects.filter(student_id=shared_user, semester="SOS")
		all_sos = chain(soph_spring, app_sos)
		junior_fall = Entry.objects.filter(student_id=shared_user, semester="JRF")
		app_jrf = Approved_Course.objects.filter(student_id=shared_user, semester="JRF")
		all_jrf = chain(junior_fall, app_jrf)
		junior_spring = Entry.objects.filter(student_id=shared_user, semester="JRS")
		app_jrs = Approved_Course.objects.filter(student_id=shared_user, semester="JRS")
		all_jrs = chain(junior_spring, app_jrs)
		senior_fall = Entry.objects.filter(student_id=shared_user, semester="SRF")
		app_srf = Approved_Course.objects.filter(student_id=shared_user, semester="SRF")
		all_srf = chain(senior_fall, app_srf)
		senior_spring = Entry.objects.filter(student_id=shared_user, semester="SRS")
		app_srs = Approved_Course.objects.filter(student_id=shared_user, semester="SRS")
		all_srs = chain(senior_spring, app_srs)

	# still need to do this
	#student_outside=[]
	#outside_courses = Outside_Course.objects.filter(student_id=shared_user) # list of the student's outside courses
	#for c in outside_courses.iterator():
	#	student_outside.append(c.course_name)

	context = {'user': current_user.username,'shared_user': shared_user, 'fresh_fall': all_frf, 'fresh_spring': all_frs, 
	'soph_fall': all_sof, 'soph_spring': all_sos, 'junior_fall': all_jrf, 'junior_spring': all_jrs,
	'senior_fall': all_srf, 'senior_spring': all_srs}#, 'student_outside': student_outside}
	return render(request, 'share.html', context, )


@login_required # Cas authentication for this url.
def certificates(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses - course ID
	cert_dict={}
	aas = AAS.objects.values_list('course_id', flat=True).order_by('course_id')
	afs = AFS.objects.values_list('course_id', flat=True).order_by('course_id')
	ams = AMS.objects.values_list('course_id', flat=True).order_by('course_id')
	nsimilar = num_compare(all_courses, aas)
	cert_dict["African American Studies"]=num_compare(all_courses, aas)
	cert_dict["African Studies"]=num_compare(all_courses, afs)
	cert_dict["American Studies"]=num_compare(all_courses, ams)
	top_3=[]
	for i in range(0, 3):
		maximum = max(cert_dict, key=lambda i: cert_dict[i])
		top_3.append(maximum)
		cert_dict.pop(maximum, None)
	context = {'top_3': top_3}
	return render(request, 'certificates.html', context)

def about(request):
	# current_user = request.user
	# student = Student.objects.get(student_id=current_user.username)
	# context = {}
	return render(request, 'about.html')
	
def cos_data(request):
	# current_user = request.user
	# student = Student.objects.get(student_id=current_user.username)
	# context = {}
	return render(request, 'cosdata.html')

@login_required # Cas authentication for this url.
# African American Studies
def aas(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses - course ID
	intro = AAS.objects.filter(intro=1).values_list('course_id', flat=True).order_by('course_id')
	survey = AAS.objects.filter(survey=1).values_list('course_id', flat=True).order_by('course_id')
	other = AAS.objects.filter(other=1).values_list('course_id', flat=True).order_by('course_id')

	intro_on = title(compare_lists(all_courses, intro)["similarities"])
	intro_off = title(compare_lists(all_courses, intro)["differences"])

	survey_on = title(compare_lists(all_courses, survey)["similarities"])
	survey_off = title(compare_lists(all_courses, survey)["differences"])

	other_on = title(compare_lists(all_courses, other)["similarities"])
	other_off = title(compare_lists(all_courses, other)["differences"])
	#other_off=[]

	context = {'intro_on': intro_on, 'intro_off': intro_off, 'survey_on': survey_on, 'survey_off': survey_off,
	'other_on': other_on, 'other_off': other_off}
	return render(request, 'aas.html', context)

@login_required # Cas authentication for this url.
# African Studies
def afs(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	foundation = AFS.objects.filter(foundation=1).values_list('course_id', flat=True).order_by('course_id')
	culture = AFS.objects.filter(culture=1).values_list('course_id', flat=True).order_by('course_id')
	history = AFS.objects.filter(history=1).values_list('course_id', flat=True).order_by('course_id')
	science = AFS.objects.filter(science=1).values_list('course_id', flat=True).order_by('course_id')
	politics = AFS.objects.filter(politics=1).values_list('course_id', flat=True).order_by('course_id')
	elective = AFS.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	foundation_on = title(compare_lists(all_courses, foundation)["similarities"])
	foundation_off = title(compare_lists(all_courses, foundation)["differences"])

	culture_on = title(compare_lists(all_courses, culture)["similarities"])
	culture_off = title(compare_lists(all_courses, culture)["differences"])

	history_on = title(compare_lists(all_courses, history)["similarities"])
	history_off = title(compare_lists(all_courses, history)["differences"])

	science_on = title(compare_lists(all_courses, science)["similarities"])
	science_off = title(compare_lists(all_courses, science)["differences"])

	politics_on = title(compare_lists(all_courses, politics)["similarities"])
	politics_off = title(compare_lists(all_courses, politics)["differences"])

	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])

	context = {'foundation_on': foundation_on, 'foundation_off': foundation_off, 'culture_on': culture_on, 'culture_off': culture_off,
	'history_on': history_on, 'history_off': history_off, 'science_on': science_on, 'science_off': science_off, 'politics_on': politics_on, 'politics_off': politics_off,
	'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'afs.html', context)

@login_required # Cas authentication for this url.
# American Studies
def ams(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	core = AMS.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	ams = AMS.objects.filter(ams=1).values_list('course_id', flat=True).order_by('course_id')
	elective = AMS.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	core_on = title(compare_lists(all_courses, core)["similarities"])
	core_off = title(compare_lists(all_courses, core)["differences"])

	ams_on = title(compare_lists(all_courses, ams)["similarities"])
	ams_off = title(compare_lists(all_courses, ams)["differences"])

	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])
	#other_off=[]

	context = {'core_on': core_on, 'core_off': core_off, 'ams_on': ams_on, 'ams_off': ams_off,
	'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'ams.html', context)

