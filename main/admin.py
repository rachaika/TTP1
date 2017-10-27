from django.contrib import admin
from .models import UserProfile,User, Tutor, Student, Availability, Sessions

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Availability)
admin.site.register(Sessions)
