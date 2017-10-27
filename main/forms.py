from django import forms
from django.contrib.auth.models import User
from main.models import UserProfile, Sessions

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=('student','tutor','avatar')


class BookingForm(forms.ModelForm):
    class Meta():
        model = Sessions
        fields = ('tutor_id', 'student_id', 'booked_time' )
