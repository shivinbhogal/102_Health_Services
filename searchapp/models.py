from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Speciality(models.Model):
	type = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.type)
		super(Speciality, self).save(*args, **kwargs)
	
	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return self.type

class Doctor(models.Model):
	speciality = models.ForeignKey(Speciality)
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=500,default='xxxxxx')
	phone_no = models.CharField(max_length=10,default='0000000000')

	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.name