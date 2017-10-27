from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    student=models.BooleanField()
    tutor=models.BooleanField()
    avatar=models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username




#class Transactions


# Create your models here.
class Tutor(models.Model):

    #tutor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=128)

    lastName = models.CharField(max_length=128)
    tutor_email = models.EmailField(max_length=254, unique=True)
    tutor_booking_status = models.BooleanField()
    is_student = models.BooleanField()
    university_name = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)    #max_digits includes number of decimal places
    tutor_intro = models.TextField()

    #available_time = models.ForeignKey(Availability,default=1, null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('tutor-detail-view', args=[str(self.id)])

    def time_slots(self):
        return ', '.join([a.start_time for a in self.available_time.all()])



class Availability(models.Model):

    tutor = models.ForeignKey(Tutor, null=True)
    WEEKDAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    #Tutor.objects.values_list('available_time__weekday')

    weekday = models.PositiveSmallIntegerField(choices=WEEKDAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name_plural = "Availabilities"

    def __str__(self):
        #return str(self.weekday) + " " + str(self.start_time) + "-" + str(self.end_time)
        return str(self.start_time)
#class Sessions

class Student(models.Model):
    #student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_first_name = models.CharField(max_length=128)
    student_last_name = models.CharField(max_length=128)
    student_email = models.EmailField(max_length=254, unique=True)
    student_booking_status = models.BooleanField()
    is_tutor = models.BooleanField()
    #tutor = models.ForeigKey(Tutor)

    def __str__(self):
        return self.student_first_name

class Sessions(models.Model):

    student_id = models.ForeignKey(Student)
    tutor_id = models.ForeignKey(Tutor)
    booked_time = models.ForeignKey(Availability, null=True)

    def __str__(self):
        return self.student_id.student_first_name + " " + str(self.booked_time.start_time) + " " + self.tutor_id.firstName

    class Meta:
        verbose_name_plural = "Sessions"
#
# class Booking(model.Model):
#
#     tutor_id = models.ForeignKey(Tutor)
#     student_id = models.ForeignKey(Student)
#     session = models.ForeignKey(Availability)
