import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_102HealthServices.settings')

import django
django.setup()

from searchapp.models import Speciality, Doctor

def populate():
	speciality_car = add_speciality('cardio')
	speciality_child=add_speciality('child')

	add_doctor(type=speciality_car,doc_name="Dr. Ahmed Khan")
	add_doctor(type=speciality_car,doc_name="Dr. Kamal Kishore",address="abc",phone_no='0')
	add_doctor(type=speciality_child,doc_name="Dr. Tarif")
	add_doctor(type=speciality_child,doc_name="Dr. Richard")

	# Print out what we have added to the doctor.
	for s in Speciality.objects.all():
		for d in Doctor.objects.filter(speciality=s):
			print "- {0} - {1}".format(str(s), str(d))

def add_doctor(type, doc_name, address='xxxxxx', phone_no='0001'):
    d = Doctor.objects.get_or_create(speciality=type, name=doc_name)[0]
    d.address=address
    d.phone_no=phone_no
    d.save()
    return d

def add_speciality(speciality):
    s = Speciality.objects.get_or_create(type=speciality)[0]
    return s

if __name__ == '__main__':
    print "Starting SearchApp population script..."
    populate()	