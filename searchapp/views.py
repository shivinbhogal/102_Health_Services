from django.shortcuts import render
from django.http import HttpResponse
from searchapp.models import Speciality
from searchapp.models import Doctor
from datetime import datetime
import json 

# Create your views here.
def index(request):
	doctors_list = Doctor.objects.order_by('name')[:5]
	speciality_list = Speciality.objects.order_by('type')[:5]
	context_dict = {'doctors': doctors_list,'speciality': speciality_list}
	# visits = request.session.get('visits')
	# if not visits:
	# 	visits = 1

	# reset_last_visit_time = False

	# last_visit = request.session.get('last_visit')

	# if last_visit:
	# 	last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
		
	# 	if (datetime.now() - last_visit_time).seconds > 0:
	# 		visits = visits + 1
	# 		reset_last_visit_time = True
	# else:
	# 	reset_last_visit_time = True

	# if reset_last_visit_time:
	# 	request.session['last_visit'] = str(datetime.now())
	# 	request.session['visits'] = visits
	# context_dict['visits'] = visits

	response = render(request,'searchapp/index.html', context_dict)
	return response
	
def about(request):
	return HttpResponse("SearchApp says here is the about page. <br/>  <a href='/searchapp/'>Index</a>")

def speciality(request, speciality_type_slug):

    context_dict = {}

    try:
        speciality = Speciality.objects.get(slug=speciality_type_slug)
        context_dict['speciality_name'] = speciality.type

        doctors = Doctor.objects.filter(speciality=speciality)

        context_dict['doctors'] = doctors
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['speciality'] = speciality
    except speciality.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'searchapp/speciality.html', context_dict)	