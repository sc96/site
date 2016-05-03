from django.shortcuts import render
from .models import Student, Course, COS_BSE, Entry, Approved_Course, Engineer, Outside_Course, AP_Credit, ROB, URB, TAS, LIN, GSS, VPL, HEL, AAS, EAS, AFS, AMS, NEU, MUS, GHP, FIN, QCB, CWR, TPP, TIC, PSE, APC, EPS, EGR, PHY, ECS, GEO, JAZ, MED, PLA, SML
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
	total = len(req_courses)
	for s in sem_cour:
		# need to put it in dict if not already in there
		#can do dictionary thing here
		if sems[s] not in req_dict:
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

# def notFound(request):
# 	return render(request, 'pagenotfound.html')
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response



@login_required # Cas authentication for this url.
def profile(request):
	current_user = request.user;

	try:
   		s = Student.objects.get(student_id=str(current_user.username)) # changed this
	except Student.DoesNotExist:
		# creating new student. default values
   		s = Student(student_id=str(current_user.username), first_name = "First", last_name = "Last", engineerBool = "1",
   		 publicBool = "1", cert1 = "NONE", cert2 = "NONE", cert3 = "NONE", calc_1 = "0", calc_2 = "0", calc_3 = "0", 
   		 lin_alg= "0", gen_chem = "0", physics = "0", cos = "0")
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
		calc_1 = request.POST["calc_1"]
		calc_2 = request.POST["calc_2"]
		calc_3 = request.POST["calc_3"]
		lin_alg = request.POST["lin_alg"]
		gen_chem = request.POST["gen_chem"]
		physics = request.POST["physics"]
		cos = request.POST["cos"]
		student.update_info(student, firstN, lastN, engineerBool, publicBool, 
			cert1, cert2, cert3, calc_1, calc_2, calc_3, lin_alg, gen_chem, physics, cos)


			
    
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
	calc_3 =  student.calc_3
	lin_alg = student.lin_alg
	gen_chem = student.gen_chem
	physics = student.physics
	cos = student.cos

	ap_dict = {"calc_1": calc_1, "calc_2": calc_2, "calc_3": calc_3, "lin_alg" : lin_alg, 'gen_chem': gen_chem, 'physics': physics, 'cos': cos}
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
	student_stln=[]
	current_user = request.user
	student = Student.objects.get(student_id=str(current_user.username))
	student_major = student.student_major
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	all_entries = Entry.objects.filter(student_id=current_user.username) #all of the student's entries
	save_other = []
	extra_other=[]
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
		elif (course.area=='STN' or course.area=='STL'):
			student_stln.append(d)
		elif(re.match(r'WRI1', course.listings)):
			student_wri.append(d)
		elif(re.match(r'(ARA|BCS|CHI|CZE|FRE|GER|HEB|HIN|ITA|JPN|KOR|LAT|POL|POR|RUS|SPA|SWA|TUR|TWI|URD)', course.listings)):
			student_foreign.append(d)
		
		if (re.search(r'MAT3|MAT4|ELE3|ELE4|PHY3|PHY4|ORF3|ORF4', course.listings)):
			if ((re.search(r'COS', course.listings)) == None):
				extra_other.append(d)

	# something to think about: COS 340 can't pop up in "Other" and in "Theory"
	# all of the requirement lists
	# can probably combine a lot of things here into one function - maybe i want the approved courses in their own list? idk
	# COS BSE Major
	if (student.engineerBool):
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
		
		# other courses
		other_theory = Outside_Course.objects.filter(student_id = student, requirement="theory")
		other_systems = Outside_Course.objects.filter(student_id = student, requirement="systems") 
		other_apps = Outside_Course.objects.filter(student_id = student, requirement="apps")
		other_other = Outside_Course.objects.filter(student_id = student, requirement="other")
		
		theory_on = compare_lists(all_courses, theory_courses)["similarities"]
		for t in all_entries.filter(req="Theory").values_list('course_id', flat=True).order_by('course_id'):
			theory_on.append(t)
		theory_on = title(theory_on)
		theory_off = title(compare_lists(all_courses, theory_courses)["differences"])
		theory_on = list(chain(other_theory, theory_on))
		while len(theory_on) > 2:
			save_other.append(theory_on.pop(0))

		
		systems_on = compare_lists(all_courses, systems_courses)["similarities"]
		for t in all_entries.filter(req="Systems").values_list('course_id', flat=True).order_by('course_id'):
			systems_on.append(t)
		systems_on = title(systems_on)
		systems_off = title(compare_lists(all_courses, systems_courses)["differences"])
		systems_on = list(chain(other_systems, systems_on))
		while len(systems_on) > 2:
			save_other.append(systems_on.pop(0))
	
	
		apps_on = compare_lists(all_courses, apps_courses)["similarities"]
		for t in all_entries.filter(req="Applications").values_list('course_id', flat=True).order_by('course_id'):
			apps_on.append(t)
		apps_on = title(apps_on)
		apps_off = title(compare_lists(all_courses, apps_courses)["differences"])
		apps_on = list(chain(other_apps, apps_on))
		while len(apps_on) > 2:
			save_other.append(apps_on.pop(0))
	
	
		iw_on = compare_lists(all_courses, iw_courses)["similarities"] #iw is for BSE only
		iw_on = title(iw_on)
		iw_off = title(compare_lists(all_courses, iw_courses)["differences"])
		while len(iw_on) > 1:
			save_other.append(iw_on.pop(0))
	
	
			# other should have all classes in "other" that the user hasn't already taken
			# will fix this bug a little later... 4/9/2016 ....!!!!
		other_on = compare_lists(all_courses, other_courses)["similarities"]
		other_on = title(other_on)
		extra_other = title(extra_other)
		#save_other = title(save_other)
		other_on = chain(other_on, save_other)
		other_on = chain(other_on, extra_other)
		other_on = list(chain(other_on, other_other))
		#for t in all_entries.filter(req="Other").values_list('course_id', flat=True).order_by('course_id'):
		#	other_on.append(t.course_id)
		other_off = title(compare_lists(all_courses, other_courses)["differences"])
	
	
		core_on = title(compare_lists(all_courses, core_courses)["similarities"])
		core_off = title(compare_lists(all_courses, core_courses)["differences"])
	
			# Need to add logic for only hilighting 2 theory courses then overflowing others into "other" section
			# Maybe don't display everything...display ones that only have "other"
	
		other_sa = Outside_Course.objects.filter(student_id = student, distribution="sa")
		other_la = Outside_Course.objects.filter(student_id = student, distribution="la")
		other_ha = Outside_Course.objects.filter(student_id = student, distribution="ha")
		other_em = Outside_Course.objects.filter(student_id = student, distribution="em")
		other_ec = Outside_Course.objects.filter(student_id = student, distribution="ec")
		#other_la_2 = Outside_Course.objects.filter(requirement="LA")
		#other_la = chain(other_la_1, other_la_2)
			# Distribution Requirements
		student_sa=title(student_sa)
		student_sa = list(chain(student_sa, other_sa))
		student_la=title(student_la)
		student_la = list(chain(student_la, other_la))
		student_ha=title(student_ha)
		student_ha = list(chain(student_ha, other_ha))
		student_em=title(student_em)
		student_em = list(chain(student_em, other_em))
		student_ec=title(student_ec)
		student_ec = list(chain(student_ec, other_ec))
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
		
		other_math1 = Outside_Course.objects.filter(student_id = student, engineer="calc_1")
		other_math2 = Outside_Course.objects.filter(student_id = student, engineer="calc_2") 
		other_math3 = Outside_Course.objects.filter(student_id = student, engineer="calc_3")
		other_cos = Outside_Course.objects.filter(student_id = student, engineer="cos")
		other_phy1 = Outside_Course.objects.filter(student_id = student, engineer="physics_mech")
		other_phy2 = Outside_Course.objects.filter(student_id = student, engineer="Physics_em")
		other_chem = Outside_Course.objects.filter(student_id = student, engineer="gen_chem")
		
		# ap credit working now
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="538").exists()):
			if (student.calc_1 == 1):
				math_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="538").values_list('course_id', flat=True)
		math_1_on = title(compare_lists(chain(all_courses, math_1_credit), math_1)["similarities"])
		math_1_off = title(compare_lists(chain(all_courses, math_1_credit), math_1)["differences"])
		math_1_on = list(chain(math_1_on, other_math1))
		#math_1_off=[]
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1029").exists()):
			if (student.calc_2 == 1):
				math_2_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1029").values_list('course_id', flat=True)
		math_2_on = title(compare_lists(map(int, chain(all_courses, math_2_credit)), math_2)["similarities"])
		math_2_off = title(compare_lists(map(int, chain(all_courses, math_2_credit)), math_2)["differences"])
		math_2_on = list(chain(math_2_on, other_math2))
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1176").exists()):
			if (student.calc_3 == 1):
				math_3_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1176").values_list('course_id', flat=True)
		math_3_on = title(compare_lists(map(int, chain(all_courses, math_3_credit)), math_3)["similarities"])
		math_3_off = title(compare_lists(map(int, chain(all_courses, math_3_credit)), math_3)["differences"])
		math_3_on = list(chain(math_3_on, other_math3))
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1160").exists()):
			if (student.lin_alg == 1):
				math_4_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1160").values_list('course_id', flat=True)
		math_4_on = title(compare_lists(map(int, chain(all_courses, math_4_credit)), math_4)["similarities"])
		math_4_off = title(compare_lists(map(int, chain(all_courses, math_4_credit)), math_4)["differences"])
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="2016").exists()):
			if (student.physics == 1):
				physics_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="2016").values_list('course_id', flat=True)
		physics_1_on = title(compare_lists(map(int, chain(all_courses, physics_1_credit)), physics_1)["similarities"])
		physics_1_off = title(compare_lists(map(int, chain(all_courses, physics_1_credit)), physics_1)["differences"])
		physics_1_on = list(chain(physics_1_on, other_phy1))
		#physics_1_on = chain(all_courses, physics_1_credit)
		#physics_1_off = physics_1
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="763").exists()):
			if (student.physics == 1):
				physics_2_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="763").values_list('course_id', flat=True)
		physics_2_on = title(compare_lists(map(int, chain(all_courses, physics_2_credit)), physics_2)["similarities"])
		physics_2_off = title(compare_lists(map(int, chain(all_courses, physics_2_credit)), physics_2)["differences"])
		physics_2_on = list(chain(physics_2_on, other_phy2))
		
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1354").exists()):
			if (student.gen_chem == 1):
				chem_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1354").values_list('course_id', flat=True)
		chem_1_on = title(compare_lists(map(int, chain(all_courses, chem_1_credit)), chem_1)["similarities"])
		chem_1_off = title(compare_lists(map(int, chain(all_courses, chem_1_credit)), chem_1)["differences"])
		chem_1_on = list(chain(chem_1_on, other_chem))
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="444").exists()):
			if (student.cos == 1):
				cos_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="444").values_list('course_id', flat=True)
		cos_1_on = title(compare_lists(map(int, chain(all_courses, cos_1_credit)), cos_1)["similarities"])
		cos_1_off = title(compare_lists(map(int, chain(all_courses, cos_1_credit)), cos_1)["differences"])
		cos_1_on = list(chain(cos_1_on, other_cos))
	
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
	else:
		math_1 = Engineer.objects.filter(math_1=1).values_list('course_id', flat=True)
		math_2 = Engineer.objects.filter(math_2=1).values_list('course_id', flat=True)
		math_3 = Engineer.objects.filter(math_3=1).values_list('course_id', flat=True)
		math_4 = Engineer.objects.filter(math_4=1).values_list('course_id', flat=True)
		
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
				# can probably shorten this a little bit later...
		theory_courses = COS_BSE.objects.filter(theory=1).values_list('course_id', flat=True).order_by('course_id')
		systems_courses = COS_BSE.objects.filter(systems=1).values_list('course_id', flat=True).order_by('course_id')
		apps_courses = COS_BSE.objects.filter(applications=1).values_list('course_id', flat=True).order_by('course_id')
		core_courses = COS_BSE.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
		other_courses = COS_BSE.objects.filter(other=1).values_list('course_id', flat=True).order_by('course_id')
		iw_courses = COS_BSE.objects.filter(iw=1).values_list('course_id', flat=True).order_by('course_id')
		
		# other courses
		other_theory = Outside_Course.objects.filter(student_id = student, requirement="theory")
		other_systems = Outside_Course.objects.filter(student_id = student, requirement="systems") 
		other_apps = Outside_Course.objects.filter(student_id = student, requirement="apps")
		other_other = Outside_Course.objects.filter(student_id = student, requirement="other")
		
		theory_on = compare_lists(all_courses, theory_courses)["similarities"]
		for t in all_entries.filter(req="Theory").values_list('course_id', flat=True).order_by('course_id'):
			theory_on.append(t)
		theory_on = title(theory_on)
		theory_off = title(compare_lists(all_courses, theory_courses)["differences"])
		theory_on = list(chain(other_theory, theory_on))
		while len(theory_on) > 2:
			save_other.append(theory_on.pop(0))

		
		systems_on = compare_lists(all_courses, systems_courses)["similarities"]
		for t in all_entries.filter(req="Systems").values_list('course_id', flat=True).order_by('course_id'):
			systems_on.append(t)
		systems_on = title(systems_on)
		systems_off = title(compare_lists(all_courses, systems_courses)["differences"])
		systems_on = list(chain(other_systems, systems_on))
		while len(systems_on) > 2:
			save_other.append(systems_on.pop(0))
	
	
		apps_on = compare_lists(all_courses, apps_courses)["similarities"]
		for t in all_entries.filter(req="Applications").values_list('course_id', flat=True).order_by('course_id'):
			apps_on.append(t)
		apps_on = title(apps_on)
		apps_off = title(compare_lists(all_courses, apps_courses)["differences"])
		apps_on = list(chain(other_apps, apps_on))
		while len(apps_on) > 2:
			save_other.append(apps_on.pop(0))
	
	
		iw_on = compare_lists(all_courses, iw_courses)["similarities"] #iw is for BSE only
		iw_on = title(iw_on)
		iw_off = title(compare_lists(all_courses, iw_courses)["differences"])
		while len(iw_on) > 4:
			save_other.append(iw_on.pop(0))
	
	
			# other should have all classes in "other" that the user hasn't already taken
			# will fix this bug a little later... 4/9/2016 ....!!!!
		other_on = compare_lists(all_courses, other_courses)["similarities"]
		other_on = title(other_on)
		extra_other = title(extra_other)
		#save_other = title(save_other)
		other_on = chain(other_on, save_other)
		other_on = chain(other_on, extra_other)
		other_on = list(chain(other_on, other_other))
		#for t in all_entries.filter(req="Other").values_list('course_id', flat=True).order_by('course_id'):
		#	other_on.append(t.course_id)
		other_off = title(compare_lists(all_courses, other_courses)["differences"])
	
	
		core_on = title(compare_lists(all_courses, core_courses)["similarities"])
		core_off = title(compare_lists(all_courses, core_courses)["differences"])
	
	
		
		math_1_credit=[0000]
		math_2_credit=[0000]
		math_3_credit=[0000]
		math_4_credit=[0000]
		physics_1_credit=[0000]
		physics_2_credit=[0000]
		chem_1_credit=[0000]
		cos_1_credit=[0000]
		
		other_math1 = Outside_Course.objects.filter(student_id = student, engineer="calc_1")
		other_math2 = Outside_Course.objects.filter(student_id = student, engineer="calc_2") 
		other_math3 = Outside_Course.objects.filter(student_id = student, engineer="calc_3")
		other_cos = Outside_Course.objects.filter(student_id = student, engineer="cos")
		other_phy1 = Outside_Course.objects.filter(student_id = student, engineer="physics_mech")
		other_phy2 = Outside_Course.objects.filter(student_id = student, engineer="Physics_em")
		other_chem = Outside_Course.objects.filter(student_id = student, engineer="gen_chem")
		
		# ap credit working now
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="538").exists()):
			if (student.calc_1 == 1):
				math_1_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="538").values_list('course_id', flat=True)
		math_1_on = title(compare_lists(chain(all_courses, math_1_credit), math_1)["similarities"])
		math_1_off = title(compare_lists(chain(all_courses, math_1_credit), math_1)["differences"])
		math_1_on = list(chain(math_1_on, other_math1))
		#math_1_off=[]
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1029").exists()):
			if (student.calc_2 == 1):
				math_2_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1029").values_list('course_id', flat=True)
		math_2_on = title(compare_lists(map(int, chain(all_courses, math_2_credit)), math_2)["similarities"])
		math_2_off = title(compare_lists(map(int, chain(all_courses, math_2_credit)), math_2)["differences"])
		math_2_on = list(chain(math_2_on, other_math2))
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1176").exists()):
			if (student.calc_3 == 1):
				math_3_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1176").values_list('course_id', flat=True)
		math_3_on = title(compare_lists(map(int, chain(all_courses, math_3_credit)), math_3)["similarities"])
		math_3_off = title(compare_lists(map(int, chain(all_courses, math_3_credit)), math_3)["differences"])
		math_3_on = list(chain(math_3_on, other_math3))
		
		if (AP_Credit.objects.filter(student_name=current_user.username, course_id="1160").exists()):
			if (student.lin_alg == 1):
				math_4_credit = AP_Credit.objects.filter(student_name=current_user.username, course_id="1160").values_list('course_id', flat=True)
		math_4_on = title(compare_lists(map(int, chain(all_courses, math_4_credit)), math_4)["similarities"])
		math_4_off = title(compare_lists(map(int, chain(all_courses, math_4_credit)), math_4)["differences"])
		
	
			# Need to add logic for only hilighting 2 theory courses then overflowing others into "other" section
			# Maybe don't display everything...display ones that only have "other"
	
	
			# Distribution Requirements
		other_sa = Outside_Course.objects.filter(student_id = student, distribution="sa")
		other_la = Outside_Course.objects.filter(student_id = student, distribution="la")
		other_ha = Outside_Course.objects.filter(student_id = student, distribution="ha")
		other_em = Outside_Course.objects.filter(student_id = student, distribution="em")
		other_ec = Outside_Course.objects.filter(student_id = student, distribution="ec")
		other_stn = Outside_Course.objects.filter(student_id = student, distribution="stn")
		other_stl = Outside_Course.objects.filter(student_id = student, distribution="stl")
		#other_la_2 = Outside_Course.objects.filter(requirement="LA")
		#other_la = chain(other_la_1, other_la_2)
			# Distribution Requirements
		student_sa=title(student_sa)
		student_sa = list(chain(student_sa, other_sa))
		student_la=title(student_la)
		student_la = list(chain(student_la, other_la))
		student_ha=title(student_ha)
		student_ha = list(chain(student_ha, other_ha))
		student_em=title(student_em)
		student_em = list(chain(student_em, other_em))
		student_ec=title(student_ec)
		student_ec = list(chain(student_ec, other_ec))
		student_stln=title(student_stln)
		student_stln = list(chain(student_stln, other_stl))
		student_stln = list(chain(student_stln, other_stn))
		student_wri=title(student_wri)
		student_foreign=title(student_foreign)
		
		context = {'theory_on': theory_on, 'theory_off': theory_off, 'systems_on': systems_on, 'systems_off': systems_off,
		'apps_on': apps_on, 'apps_off': apps_off, 'other_on': other_on, 'other_off': other_off,
		'iw_on': iw_on, 'iw_off': iw_off, 'core_on': core_on, 'core_off': core_off, 'student_stln': student_stln,
		'student_sa': student_sa, 'student_la': student_la, 'student_ha': student_ha, 'student_ec': student_ec,
		'student_em': student_em, 'student_foreign': student_foreign, 'student_wri': student_wri,
		'math_1_on': math_1_on, 'math_1_off': math_1_off, 'math_2_on': math_2_on, 'math_2_off': math_2_off, 'math_3_on': math_3_on, 'math_3_off': math_3_off,
		'math_4_on': math_4_on, 'math_4_off': math_4_off}#, 'cos_1': cos_1}
		return render(request, 'degree_progress_cos_ab.html', context)

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
   		s = Student(student_id=current_user.username)
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

		elif 'removeSummer' in request.POST:
			removed_class = request.POST['removeSummer']
			student.remove_courseSummer(removed_class, student)
			

		else:
			added_class = request.POST['listing']
			added_class = Course.objects.get(listings=added_class)
			semester = request.POST['semester']
			sem = time[semester]
			req = request.POST['COSreq']
			student.add_course(added_class, student, sem, req)
		#add_class(student, added_class, semester)
	#Return matched courses for search bar
	matched_courses = ""
	if request.method == 'GET':
		if 'the_query' in request.GET:
			query_text = request.GET.get('the_query')
			matched_courses = course_search(query_text)
			context['matched_courses'] = matched_courses
			return HttpResponse(
            json.dumps(),
            content_type="application/json"
        )
	# if 'q' in request.GET:
	# 	test = request.GET["q"]
	# matched_courses = course_search(test);
	
	# getting list of courses for each semester
	fresh_fall = Entry.objects.filter(student_id=current_user.username, semester="FRF")
	app_frf = Approved_Course.objects.filter(student_id=current_user.username, semester="FRF")
	all_frf = chain(fresh_fall, app_frf)
	fresh_spring = Entry.objects.filter(student_id=current_user.username, semester="FRS")
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
	#for c in outside_courses.iterator():
	#	student_outside.append(c.course_name)

	context = {'user': current_user.username,'fresh_fall': all_frf, 'fresh_spring': all_frs, 
	'soph_fall': all_sof, 'soph_spring': all_sos, 'junior_fall': all_jrf, 'junior_spring': all_jrs,
	'senior_fall': all_srf, 'senior_spring': all_srs, 'student_outside': outside_courses,'test': test, 'matched_courses': matched_courses, 'test_course': added_class, 'sem': semester,
	 'removed_class': removed_class }
	return render(request, 'four_year.html', context, )




@login_required # Cas authentication for this url.
# if you got a course at Princeton to count as a COS departmental
def outside_course_approval(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	context = {}

	if request.method == 'POST':
		title = ""
		COSreq = "na"
		BSEreq = "na"
		distr = "na"
		if 'course_title' in request.POST:
			title = request.POST['course_title']
			context['title'] = title
			if "COSreq" in request.POST:
				COSreq = request.POST["COSreq"]
				context['COSreq'] = COSreq
			if "BSEreq" in request.POST:
				BSEreq = request.POST["BSEreq"]
				# if BSEreq == "calc_1":
				# 	student.calc_1 = "1"
				# elif BSEreq == "calc_2":
				# 	student.calc_2 = "1"
				# elif BSEreq == "calc_3":
				# 	student.calc_3 = "1"
				# elif BSEreq == "cos":
				# 	student.cos = "1"
				# elif BSEreq == "gen_chem":
				# 	student.gen_chem = "1"
				# elif BSEreq == "physics_mech":
				# 	student.physics = "1"				#HELLLP - Need to break into semesters
				# elif BSEreq == "physics_em":
				# 	student.physics = "1"
				# else:
				# 	continue
				#student.save()
				context['BSEreq'] = BSEreq
			if "Distribution" in request.POST:
				distr = request.POST["Distribution"]
				context['distr'] = distr
		student.add_outside_course(title, student, COSreq, distr, BSEreq)
	
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
	#length = len(points_dict)
	top_5=[]
	for i in range(0, 11):
		if(points_dict.keys()):
			maximum = max(points_dict, key=lambda i: points_dict[i])
			if (Student.objects.get(student_id=maximum).publicBool):
				top_5.append(maximum)
			else:
				top_5.append("Student" + str(Student.objects.get(student_id=maximum).id))
			points_dict.pop(maximum, None)
	# then can do a generic thing for clicking on one of top 5 students and it shows you their four year
	top_5.pop(0)
	length = len(top_5)
	length = top_5[9]
	context = {'user': current_user.username,'nStudents': nStudents, 'len': length, 'top_5': top_5}
	return render(request, 'sharing.html', context)


@login_required # Cas authentication for this url.
def share(request, shared_user):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	if (re.match(r'Student', shared_user)):
		num = int(str(shared_user[7:]))
		stu = Student.objects.get(id=num).student_id
		fresh_fall = Entry.objects.filter(student_id=stu, semester="FRF")
		#app_frf = Approved_Course.objects.filter(id=num, semester="FRF")
		#app_frf=[]
		all_frf = fresh_fall#chain(fresh_fall, app_frf)
		fresh_spring = Entry.objects.filter(student_id=stu, semester="FRS")
		#app_frs = Approved_Course.objects.filter(id=num, semester="FRS")
		#app_frs=[]
		all_frs = fresh_spring# chain(fresh_spring, app_frs)
		soph_fall = Entry.objects.filter(student_id=stu, semester="SOF")
		#app_sof = Approved_Course.objects.filter(id=num, semester="SOF")
		#app_sof=[]
		all_sof = soph_fall#chain(soph_fall, app_sof)
		soph_spring = Entry.objects.filter(student_id=stu, semester="SOS")
		#app_sos = Approved_Course.objects.filter(id=num, semester="SOS")
		#app_sos=[]
		all_sos = soph_spring#chain(soph_spring, app_sos)
		junior_fall = Entry.objects.filter(student_id=stu, semester="JRF")
		#app_jrf = Approved_Course.objects.filter(id=num, semester="JRF")
		#app_jrf=[]
		all_jrf = junior_fall#chain(junior_fall, app_jrf)
		junior_spring = Entry.objects.filter(student_id=stu, semester="JRS")
		#app_jrs = Approved_Course.objects.filter(id=num, semester="JRS")
		#app_jrs=[]
		all_jrs = junior_spring#chain(junior_spring, app_jrs)
		senior_fall = Entry.objects.filter(student_id=stu, semester="SRF")
		#app_srf = Approved_Course.objects.filter(id=num, semester="SRF")
		#app_srf=[]
		all_srf = senior_fall#chain(senior_fall, app_srf)
		senior_spring = Entry.objects.filter(student_id=stu, semester="SRS")
		#app_srs = Approved_Course.objects.filter(id=num, semester="SRS")
		#app_srs=[]
		all_srs = senior_spring#chain(senior_spring, app_srs)
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


	# otherstudent = Student.objects.get(student_id=shared_user)

	# if (otherstudent.publicBool == 1):
	context = {'user': current_user.username,'shared_user': shared_user, 'fresh_fall': all_frf, 'fresh_spring': all_frs, 
	'soph_fall': all_sof, 'soph_spring': all_sos, 'junior_fall': all_jrf, 'junior_spring': all_jrs,
	'senior_fall': all_srf, 'senior_spring': all_srs}#, 'student_outside': student_outside}
	return render(request, 'share.html', context)

	#else:
	#	context = {'user': current_user.username}
	#	return render(request, 'private.html', context)



@login_required # Cas authentication for this url.
def certificates(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses - course ID
	cert_dict={}
	aas = AAS.objects.values_list('course_id', flat=True).order_by('course_id')
	afs = AFS.objects.values_list('course_id', flat=True).order_by('course_id')
	ams = AMS.objects.values_list('course_id', flat=True).order_by('course_id')
	fin = FIN.objects.values_list('course_id', flat=True).order_by('course_id')
	ghp = GHP.objects.values_list('course_id', flat=True).order_by('course_id')
	mus = MUS.objects.values_list('course_id', flat=True).order_by('course_id')
	neu = NEU.objects.values_list('course_id', flat=True).order_by('course_id')
	cwr = CWR.objects.values_list('course_id', flat=True).order_by('course_id')
	qcb = QCB.objects.values_list('course_id', flat=True).order_by('course_id')
	eas = EAS.objects.values_list('course_id', flat=True).order_by('course_id')
	rob = ROB.objects.values_list('course_id', flat=True).order_by('course_id')
	vpl = VPL.objects.values_list('course_id', flat=True).order_by('course_id')
	hel = HEL.objects.values_list('course_id', flat=True).order_by('course_id')
	
	apc = APC.objects.values_list('course_id', flat=True).order_by('course_id')
	eps = EPS.objects.values_list('course_id', flat=True).order_by('course_id')
	egr = EGR.objects.values_list('course_id', flat=True).order_by('course_id')
	phy = PHY.objects.values_list('course_id', flat=True).order_by('course_id')
	ecs = ECS.objects.values_list('course_id', flat=True).order_by('course_id')
	geo = GEO.objects.values_list('course_id', flat=True).order_by('course_id')
	jaz = JAZ.objects.values_list('course_id', flat=True).order_by('course_id')
	med = MED.objects.values_list('course_id', flat=True).order_by('course_id')
	pla = PLA.objects.values_list('course_id', flat=True).order_by('course_id')
	sml = SML.objects.values_list('course_id', flat=True).order_by('course_id')
	pse = PSE.objects.values_list('course_id', flat=True).order_by('course_id')
	tpp = TPP.objects.values_list('course_id', flat=True).order_by('course_id')
	tas = TAS.objects.values_list('course_id', flat=True).order_by('course_id')
	tic = TIC.objects.values_list('course_id', flat=True).order_by('course_id')
	
	nsimilar = num_compare(all_courses, aas)
	cert_dict["African American Studies"]=num_compare(all_courses, aas)
	cert_dict["African Studies"]=num_compare(all_courses, afs)
	cert_dict["American Studies"]=num_compare(all_courses, ams)
	cert_dict["Neuroscience"]=num_compare(all_courses, neu)
	cert_dict["Musical Performance"]=num_compare(all_courses, mus)
	cert_dict["Global Health and Health Policy"]=num_compare(all_courses, ghp)
	cert_dict["Finance"]=num_compare(all_courses, fin)
	cert_dict["Creative Writing"]=num_compare(all_courses, cwr)
	cert_dict["Quantitative and Computational Biology"]=num_compare(all_courses, qcb)
	cert_dict["East Asian Studies"]=num_compare(all_courses, eas)
	cert_dict["Robotics and Intelligent Systems"]=num_compare(all_courses, rob)
	cert_dict["Values and Public Life"]=num_compare(all_courses, vpl)
	cert_dict["Hellenic Studies"]=num_compare(all_courses, hel)
	
	cert_dict["Applications of Computing"]=num_compare(all_courses, apc)
	cert_dict["Contemporary European Politics and Society"]=num_compare(all_courses, eps)
	cert_dict["Engineering and Management Systems"]=num_compare(all_courses, egr)
	cert_dict["Engineering Physics"]=num_compare(all_courses, phy)
	cert_dict["European Cultural Studies"]=num_compare(all_courses, ecs)
	cert_dict["Geological Engineering"]=num_compare(all_courses, geo)
	cert_dict["Jazz Studies"]=num_compare(all_courses, jaz)
	cert_dict["Sustainable Energy"]=num_compare(all_courses, pse)
	cert_dict["Medieval Studies"]=num_compare(all_courses, med)
	cert_dict["Planets and Life"]=num_compare(all_courses, pla)
	cert_dict["Statistics and Machine Learning"]=num_compare(all_courses, sml)
	cert_dict["Teacher Preparation"]=num_compare(all_courses, tpp)
	cert_dict["Technology and Society"]=num_compare(all_courses, tas)
	cert_dict["Translation and Intercultural Communication"]=num_compare(all_courses, tic)
	
	top_3=[]
	for i in range(0, 5):
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

@login_required # Cas authentication for this url.
# African Studies
def fin(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	mat = FIN.objects.filter(mat=1).values_list('course_id', flat=True).order_by('course_id')
	eco = FIN.objects.filter(eco=1).values_list('course_id', flat=True).order_by('course_id')
	stat = FIN.objects.filter(stat=1).values_list('course_id', flat=True).order_by('course_id')
	core = FIN.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	elective = FIN.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	mat_on = title(compare_lists(all_courses, mat)["similarities"])
	mat_off = title(compare_lists(all_courses, mat)["differences"])

	eco_on = title(compare_lists(all_courses, eco)["similarities"])
	eco_off = title(compare_lists(all_courses, eco)["differences"])

	stat_on = title(compare_lists(all_courses, stat)["similarities"])
	stat_off = title(compare_lists(all_courses, stat)["differences"])

	core_on = title(compare_lists(all_courses, core)["similarities"])
	core_off = title(compare_lists(all_courses, core)["differences"])

	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])

	context = {'mat_on': mat_on, 'mat_off': mat_off, 'eco_on': eco_on, 'eco_off': eco_off,
	'stat_on': stat_on, 'stat_off': stat_off, 'core_on': core_on, 'core_off': core_off,
	'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'fin.html', context)


@login_required # Cas authentication for this url.
# African Studies
def ghp(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	science = GHP.objects.filter(science=1).values_list('course_id', flat=True).order_by('course_id')
	stats = GHP.objects.filter(stats=1).values_list('course_id', flat=True).order_by('course_id')
	core = GHP.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	elective = GHP.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	science_on = title(compare_lists(all_courses, science)["similarities"])
	science_off = title(compare_lists(all_courses, science)["differences"])

	stats_on = title(compare_lists(all_courses, stats)["similarities"])
	stats_off = title(compare_lists(all_courses, stats)["differences"])

	core_on = title(compare_lists(all_courses, core)["similarities"])
	core_off = title(compare_lists(all_courses, core)["differences"])

	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])

	context = {'science_on': science_on, 'science_off': science_off, 'stats_on': stats_on, 'stats_off': stats_off,
	'core_on': core_on, 'core_off': core_off, 'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'ghp.html', context)

@login_required # Cas authentication for this url.
# African Studies
def urb(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	intro = URB.objects.filter(intro=1).values_list('course_id', flat=True).order_by('course_id')
	social = URB.objects.filter(social=1).values_list('course_id', flat=True).order_by('course_id')
	human = URB.objects.filter(human=1).values_list('course_id', flat=True).order_by('course_id')
	engineer = URB.objects.filter(engineer=1).values_list('course_id', flat=True).order_by('course_id')

	intro_on = title(compare_lists(all_courses, intro)["similarities"])
	intro_off = title(compare_lists(all_courses, intro)["differences"])

	social_on = title(compare_lists(all_courses, social)["similarities"])
	social_off = title(compare_lists(all_courses, social)["differences"])

	human_on = title(compare_lists(all_courses, human)["similarities"])
	human_off = title(compare_lists(all_courses, human)["differences"])

	engineer_on = title(compare_lists(all_courses, engineer)["similarities"])
	engineer_off = title(compare_lists(all_courses, engineer)["differences"])

	context = {'intro_on': intro_on, 'intro_off': intro_off, 'social_on': social_on, 'social_off': social_off,
	'human_on': human_on, 'human_off': human_off, 'engineer_on': engineer_on, 'engineer_off': engineer_off}
	return render(request, 'urb.html', context)


@login_required # Cas authentication for this url.
# African Studies
def cwr(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	two = CWR.objects.filter(two=1).values_list('course_id', flat=True).order_by('course_id')
	three = CWR.objects.filter(three=1).values_list('course_id', flat=True).order_by('course_id')
	
	two_on = title(compare_lists(all_courses, two)["similarities"])
	two_off = title(compare_lists(all_courses, two)["differences"])

	three_on = title(compare_lists(all_courses, three)["similarities"])
	three_off = title(compare_lists(all_courses, three)["differences"])

	context = {'two_on': two_on, 'two_off': two_off, 'three_on': three_on, 'three_off': three_off}
	return render(request, 'cwr.html', context)

@login_required
def mus(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	intro = MUS.objects.filter(intro=1).values_list('course_id', flat=True).order_by('course_id')
	perform = MUS.objects.filter(perform=1).values_list('course_id', flat=True).order_by('course_id')
	elective = MUS.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	intro_on = title(compare_lists(all_courses, intro)["similarities"])
	intro_off = title(compare_lists(all_courses, intro)["differences"])

	perform_on = title(compare_lists(all_courses, perform)["similarities"])
	perform_off = title(compare_lists(all_courses, perform)["differences"])

	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])

	context = {'intro_on': intro_on, 'intro_off': intro_off, 'perform_on': perform_on, 'perform_off': perform_off,
	'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'mus.html', context)

@login_required
def hum(request):
	context = []
	return render(request, 'hum.html', context)

@login_required
def rus(request):
	context = []
	return render(request, 'rus.html', context)

@login_required
def bio(request):
	context = []
	return render(request, 'bio.html', context)

@login_required
def arc(request):
	context = []
	return render(request, 'arc.html', context)

@login_required
def apm(request):
	context = []
	return render(request, 'apm.html', context)
	
@login_required
def apc(request):
	context = []
	return render(request, 'apc.html', context)

@login_required
def env(request):
	context = []
	return render(request, 'env.html', context)

@login_required
def mat(request):
	context = []
	return render(request, 'mat.html', context)

@login_required
def dan(request):
	context = []
	return render(request, 'dan.html', context)
	
@login_required
def sas(request):
	context = []
	return render(request, 'sas.html', context)
	
@login_required
def lac(request):
	context = []
	return render(request, 'lac.html', context)
	
@login_required
def nes(request):
	context = []
	return render(request, 'nes.html', context)

@login_required
def egb(request):
	context = []
	return render(request, 'egb.html', context)
	
	
@login_required
def jud(request):
	context = []
	return render(request, 'jud.html', context)
	
@login_required
def vis(request):
	context = []
	return render(request, 'vis.html', context)
	
@login_required
def thr(request):
	context = []
	return render(request, 'thr.html', context)

@login_required
def lao(request):
	context = []
	return render(request, 'lao.html', context)
	
@login_required
def las(request):
	context = []
	return render(request, 'las.html', context)

@login_required
def neu(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	req = NEU.objects.filter(req=1).values_list('course_id', flat=True).order_by('course_id')
	disease = NEU.objects.filter(disease=1).values_list('course_id', flat=True).order_by('course_id')
	circuits = NEU.objects.filter(circuits=1).values_list('course_id', flat=True).order_by('course_id')
	social = NEU.objects.filter(social=1).values_list('course_id', flat=True).order_by('course_id')

	req_on = title(compare_lists(all_courses, req)["similarities"])
	req_off = title(compare_lists(all_courses, req)["differences"])

	disease_on = title(compare_lists(all_courses, disease)["similarities"])
	disease_off = title(compare_lists(all_courses, disease)["differences"])

	circuits_on = title(compare_lists(all_courses, circuits)["similarities"])
	circuits_off = title(compare_lists(all_courses, circuits)["differences"])
	
	social_on = title(compare_lists(all_courses, social)["similarities"])
	social_off = title(compare_lists(all_courses, social)["differences"])

	context = {'req_on': req_on, 'req_off': req_off, 'disease_on': disease_on, 'disease_off': disease_off,
	'circuits_on': circuits_on, 'circuits_off': circuits_off, 'social_on': social_on, 'social_off': social_off}
	return render(request, 'neu.html', context)

@login_required
def pse(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	a1 = PSE.objects.filter(a1=1).values_list('course_id', flat=True).order_by('course_id')
	a2 = PSE.objects.filter(a2=1).values_list('course_id', flat=True).order_by('course_id')
	b1 = PSE.objects.filter(b1=1).values_list('course_id', flat=True).order_by('course_id')
	b2 = PSE.objects.filter(b2=1).values_list('course_id', flat=True).order_by('course_id')

	a1_on = title(compare_lists(all_courses, a1)["similarities"])
	a1_off = title(compare_lists(all_courses, a1)["differences"])

	a2_on = title(compare_lists(all_courses, a2)["similarities"])
	a2_off = title(compare_lists(all_courses, a2)["differences"])

	b1_on = title(compare_lists(all_courses, b1)["similarities"])
	b1_off = title(compare_lists(all_courses, b1)["differences"])
	
	b2_on = title(compare_lists(all_courses, b2)["similarities"])
	b2_off = title(compare_lists(all_courses, b2)["differences"])

	context = {'a1_on': a1_on, 'a1_off': a1_off, 'b1_on': b1_on, 'b1_off': b1_off,
	'a2_on': a2_on, 'a2_off': a2_off, 'b2_on': b2_on, 'b2_off': b2_off}
	return render(request, 'pse.html', context)
	
@login_required
def tpp(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	req = TPP.objects.filter(list_1=1).values_list('course_id', flat=True).order_by('course_id')

	req_on = title(compare_lists(all_courses, req)["similarities"])
	req_off = title(compare_lists(all_courses, req)["differences"])


	context = {'req_on': req_on, 'req_off': req_off}
	return render(request, 'tpp.html', context)
	
@login_required
def tic(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = TIC.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = TIC.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off}
	return render(request, 'tic.html', context)
	
@login_required
def vpl(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	core_1 = VPL.objects.filter(core_1=1).values_list('course_id', flat=True).order_by('course_id')
	core_2 = VPL.objects.filter(core_2=1).values_list('course_id', flat=True).order_by('course_id')
	core_3 = VPL.objects.filter(core_3=1).values_list('course_id', flat=True).order_by('course_id')

	core_1_on = title(compare_lists(all_courses, core_1)["similarities"])
	core_1_off = title(compare_lists(all_courses, core_1)["differences"])

	core_2_on = title(compare_lists(all_courses, core_2)["similarities"])
	core_2_off = title(compare_lists(all_courses, core_2)["differences"])

	core_3_on = title(compare_lists(all_courses, core_3)["similarities"])
	core_3_off = title(compare_lists(all_courses, core_3)["differences"])
	
	context = {'core_1_on': core_1_on, 'core_1_off': core_1_off, 'core_2_on': core_2_on, 'core_2_off': core_2_off,
	'core_3_on': core_3_on, 'core_3_off': core_3_off}
	return render(request, 'vpl.html', context)
	
@login_required
def qcb(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	isc = QCB.objects.filter(isc=1).values_list('course_id', flat=True).order_by('course_id')
	regular = QCB.objects.filter(regular=1).values_list('course_id', flat=True).order_by('course_id')
	research = QCB.objects.filter(research=1).values_list('course_id', flat=True).order_by('course_id')
	elective = QCB.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	isc_on = title(compare_lists(all_courses, isc)["similarities"])
	isc_off = title(compare_lists(all_courses, isc)["differences"])

	regular_on = title(compare_lists(all_courses, regular)["similarities"])
	regular_off = title(compare_lists(all_courses, regular)["differences"])

	research_on = title(compare_lists(all_courses, research)["similarities"])
	research_off = title(compare_lists(all_courses, research)["differences"])
	
	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])

	context = {'isc_on': isc_on, 'isc_off': isc_off, 'regular_on': regular_on, 'regular_off': regular_off,
	'research_on': research_on, 'research_off': research_off, 'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'qcb.html', context)
	
@login_required
def eas(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	chin = EAS.objects.filter(chin=1).values_list('course_id', flat=True).order_by('course_id')
	japan = EAS.objects.filter(japan=1).values_list('course_id', flat=True).order_by('course_id')
	korean = EAS.objects.filter(korean=1).values_list('course_id', flat=True).order_by('course_id')
	upper = EAS.objects.filter(upper=1).values_list('course_id', flat=True).order_by('course_id')

	chin_on = title(compare_lists(all_courses, chin)["similarities"])
	chin_off = title(compare_lists(all_courses, chin)["differences"])

	japan_on = title(compare_lists(all_courses, japan)["similarities"])
	japan_off = title(compare_lists(all_courses, japan)["differences"])

	korean_on = title(compare_lists(all_courses, korean)["similarities"])
	korean_off = title(compare_lists(all_courses, korean)["differences"])
	
	upper_on = title(compare_lists(all_courses, upper)["similarities"])
	upper_off = title(compare_lists(all_courses, upper)["differences"])

	context = {'chin_on': chin_on, 'chin_off': chin_off, 'japan_on': japan_on, 'japan_off': japan_off,
	'korean_on': korean_on, 'korean_off': korean_off, 'upper_on': upper_on, 'upper_off': upper_off}
	return render(request, 'eas.html', context)	
	
@login_required
def gss(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	intro = GSS.objects.filter(intro=1).values_list('course_id', flat=True).order_by('course_id')
	gss = GSS.objects.filter(gss=1).values_list('course_id', flat=True).order_by('course_id')

	intro_on = title(compare_lists(all_courses, intro)["similarities"])
	intro_off = title(compare_lists(all_courses, intro)["differences"])

	gss_on = title(compare_lists(all_courses, gss)["similarities"])
	gss_off = title(compare_lists(all_courses, gss)["differences"])

	context = {'intro_on': intro_on, 'intro_off': intro_off, 'gss_on': gss_on, 'gss_off': gss_off}
	return render(request, 'gss.html', context)
	
@login_required
def hel(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	admission = HEL.objects.filter(admission=1).values_list('course_id', flat=True).order_by('course_id')
	sems = HEL.objects.filter(sems=1).values_list('course_id', flat=True).order_by('course_id')

	admission_on = title(compare_lists(all_courses, admission)["similarities"])
	admission_off = title(compare_lists(all_courses, admission)["differences"])

	sems_on = title(compare_lists(all_courses, sems)["similarities"])
	sems_off = title(compare_lists(all_courses, sems)["differences"])

	context = {'admission_on': admission_on, 'admission_off': admission_off, 'sems_on': sems_on, 'sems_off': sems_off}
	return render(request, 'hel.html', context)
	
@login_required
def rob(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	lab = ROB.objects.filter(lab=1).values_list('course_id', flat=True).order_by('course_id')
	control = ROB.objects.filter(control=1).values_list('course_id', flat=True).order_by('course_id')
	cog = ROB.objects.filter(cog=1).values_list('course_id', flat=True).order_by('course_id')
	elective = ROB.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	lab_on = title(compare_lists(all_courses, lab)["similarities"])
	lab_off = title(compare_lists(all_courses, lab)["differences"])

	control_on = title(compare_lists(all_courses, control)["similarities"])
	control_off = title(compare_lists(all_courses, control)["differences"])

	cog_on = title(compare_lists(all_courses, cog)["similarities"])
	cog_off = title(compare_lists(all_courses, cog)["differences"])
	
	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])

	context = {'lab_on': lab_on, 'lab_off': lab_off, 'control_on': control_on, 'control_off': control_off,
	'cog_on': cog_on, 'cog_off': cog_off, 'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'rob.html', context)

@login_required
def lin(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	intro = LIN.objects.filter(intro=1).values_list('course_id', flat=True).order_by('course_id')
	elective = LIN.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	intro_on = title(compare_lists(all_courses, intro)["similarities"])
	intro_off = title(compare_lists(all_courses, intro)["differences"])

	elective_on = title(compare_lists(all_courses, elective)["similarities"])
	elective_off = title(compare_lists(all_courses, elective)["differences"])

	context = {'intro_on': intro_on, 'intro_off': intro_off, 'elective_on': elective_on, 'elective_off': elective_off}
	return render(request, 'lin.html', context)

@login_required
def apc(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = APC.objects.filter(pre=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = APC.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	l3 = APC.objects.filter(dept=1).values_list('course_id', flat=True).order_by('course_id')
	l4 = APC.objects.filter(outside=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	l3_on = title(compare_lists(all_courses, l3)["similarities"])
	l3_off = title(compare_lists(all_courses, l3)["differences"])
	
	l4_on = title(compare_lists(all_courses, l4)["similarities"])
	l4_off = title(compare_lists(all_courses, l4)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off,
	'l3_on': l3_on, 'l3_off': l3_off, 'l4_on': l4_on, 'l4_off': l4_off}
	return render(request, 'apc.html', context)
	
def eps(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = EPS.objects.filter(sem=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = EPS.objects.filter(culture=1).values_list('course_id', flat=True).order_by('course_id')
	l3 = EPS.objects.filter(history=1).values_list('course_id', flat=True).order_by('course_id')
	l4 = EPS.objects.filter(social=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	l3_on = title(compare_lists(all_courses, l3)["similarities"])
	l3_off = title(compare_lists(all_courses, l3)["differences"])
	
	l4_on = title(compare_lists(all_courses, l4)["similarities"])
	l4_off = title(compare_lists(all_courses, l4)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off,
	'l3_on': l3_on, 'l3_off': l3_off, 'l4_on': l4_on, 'l4_off': l4_off}
	return render(request, 'eps.html', context)
	
def egr(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = EGR.objects.filter(stats=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = EGR.objects.filter(opt=1).values_list('course_id', flat=True).order_by('course_id')
	l3 = EGR.objects.filter(prob=1).values_list('course_id', flat=True).order_by('course_id')
	l4 = EGR.objects.filter(uncert=1).values_list('course_id', flat=True).order_by('course_id')
	l5 = EGR.objects.filter(manage=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	l3_on = title(compare_lists(all_courses, l3)["similarities"])
	l3_off = title(compare_lists(all_courses, l3)["differences"])
	
	l4_on = title(compare_lists(all_courses, l4)["similarities"])
	l4_off = title(compare_lists(all_courses, l4)["differences"])

	l5_on = title(compare_lists(all_courses, l5)["similarities"])
	l5_off = title(compare_lists(all_courses, l5)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off,
	'l3_on': l3_on, 'l3_off': l3_off, 'l4_on': l4_on, 'l4_off': l4_off,  'l5_on': l5_on, 'l5_off': l5_off}
	return render(request, 'egr.html', context)

def phy(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = PHY.objects.filter(mat=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = PHY.objects.filter(phy=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off}
	return render(request, 'phy.html', context)

def ecs(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = ECS.objects.filter(intro=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = ECS.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])


	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off}
	return render(request, 'ecs.html', context)
	
def geo(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = GEO.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])


	context = {'l1_on': l1_on, 'l1_off': l1_off}
	return render(request, 'geo.html', context)
	
def jaz(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = JAZ.objects.filter(history=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = JAZ.objects.filter(theory=1).values_list('course_id', flat=True).order_by('course_id')
	l3 = JAZ.objects.filter(performance=1).values_list('course_id', flat=True).order_by('course_id')
	l4 = JAZ.objects.filter(culture=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	l3_on = title(compare_lists(all_courses, l3)["similarities"])
	l3_off = title(compare_lists(all_courses, l3)["differences"])
	
	l4_on = title(compare_lists(all_courses, l4)["similarities"])
	l4_off = title(compare_lists(all_courses, l4)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off,
	'l3_on': l3_on, 'l3_off': l3_off, 'l4_on': l4_on, 'l4_off': l4_off}
	return render(request, 'jaz.html', context)
	
def eps(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = EPS.objects.filter(sem=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = EPS.objects.filter(culture=1).values_list('course_id', flat=True).order_by('course_id')
	l3 = EPS.objects.filter(history=1).values_list('course_id', flat=True).order_by('course_id')
	l4 = EPS.objects.filter(social=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	l3_on = title(compare_lists(all_courses, l3)["similarities"])
	l3_off = title(compare_lists(all_courses, l3)["differences"])
	
	l4_on = title(compare_lists(all_courses, l4)["similarities"])
	l4_off = title(compare_lists(all_courses, l4)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off,
	'l3_on': l3_on, 'l3_off': l3_off, 'l4_on': l4_on, 'l4_off': l4_off}
	return render(request, 'eps.html', context)
	
def med(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = MED.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = MED.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])


	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off}
	return render(request, 'med.html', context)
	
def sml(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = SML.objects.filter(stats=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = SML.objects.filter(machine=1).values_list('course_id', flat=True).order_by('course_id')
	l3 = SML.objects.filter(electives=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	l3_on = title(compare_lists(all_courses, l3)["similarities"])
	l3_off = title(compare_lists(all_courses, l3)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off,
	'l3_on': l3_on, 'l3_off': l3_off}
	return render(request, 'sml.html', context)
	
def pla(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = PLA.objects.filter(intro=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = PLA.objects.filter(elective=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])


	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off}
	return render(request, 'pla.html', context)
	
def tas(request):
	current_user = request.user
	student = Student.objects.get(student_id=current_user.username)
	all_courses = Entry.objects.filter(student_id=current_user.username).values_list('course_id', flat=True).order_by('course_id') # all of the student's courses
	l1 = TAS.objects.filter(core=1).values_list('course_id', flat=True).order_by('course_id')
	l2 = TAS.objects.filter(technology=1).values_list('course_id', flat=True).order_by('course_id')
	l3 = TAS.objects.filter(societal=1).values_list('course_id', flat=True).order_by('course_id')
	l4 = TAS.objects.filter(breadth_t=1).values_list('course_id', flat=True).order_by('course_id')
	l5 = TAS.objects.filter(breadth_s=1).values_list('course_id', flat=True).order_by('course_id')

	l1_on = title(compare_lists(all_courses, l1)["similarities"])
	l1_off = title(compare_lists(all_courses, l1)["differences"])

	l2_on = title(compare_lists(all_courses, l2)["similarities"])
	l2_off = title(compare_lists(all_courses, l2)["differences"])

	l3_on = title(compare_lists(all_courses, l3)["similarities"])
	l3_off = title(compare_lists(all_courses, l3)["differences"])
	
	l4_on = title(compare_lists(all_courses, l4)["similarities"])
	l4_off = title(compare_lists(all_courses, l4)["differences"])

	l5_on = title(compare_lists(all_courses, l5)["similarities"])
	l5_off = title(compare_lists(all_courses, l5)["differences"])

	context = {'l1_on': l1_on, 'l1_off': l1_off, 'l2_on': l2_on, 'l2_off': l2_off,
	'l3_on': l3_on, 'l3_off': l3_off, 'l4_on': l4_on, 'l4_off': l4_off,  'l5_on': l5_on, 'l5_off': l5_off}
	return render(request, 'tas.html', context)
