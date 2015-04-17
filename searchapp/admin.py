from django.contrib import admin
from searchapp.models import Speciality, Doctor

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('type',)}

admin.site.register(Speciality,CategoryAdmin)
admin.site.register(Doctor)
