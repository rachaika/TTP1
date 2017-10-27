from django.shortcuts import render
from main.models import UserProfile
from main.forms import UserForm, UserProfileInfoForm
from . import models
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.generic import View,ListView,DetailView,TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from main.models import UserProfile, Availability, Sessions, Student, Tutor
from main.forms import UserForm, UserProfileInfoForm, BookingForm
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'


@login_required
def user_logout(request):
    logout(request)
    return render(request,'index.html',{})


def register(request): #Authorisation view using the built in Django authorisation model.
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered=True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request, 'main/registration.html', {'user_form':user_form, 'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'index.html',{})
                # return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT INACTIVE")
        else:
            print("Login failed")
            return HttpResponse("Invalid login details")
    else:
        return render(request,'main/login.html',{})


class TutorListView(ListView):
    context_object_name = 'tutors'
    model = models.Tutor

class TutorDetailView(DetailView):
    context_object_name = 'tutor_details'
    model = models.Tutor
    template_name = 'main/tutor_detail.html'



    #Tutor.objects.values_list('available_time__weekday')
def bookSession(request):
    # basically if there is a post request take that student_id, tutor id and time slot and save it in session.
    form = request.POST

    sid = Student.objects.get(student_first_name='stud')
    tid = Tutor.objects.get(firstName='SG')
    slot = Availability.objects.filter(tutor_id = tid)

    if request.method == 'POST':
        selected_slot = get_object_or_404(Availability, pk=request.POST.get('slot_id'))
        #Sessions.booked_time = selected_slot
        Sessions_instance = Sessions.objects.create(tutor_id=tid, student_id=sid, booked_time=selected_slot)

    #return render(request, self.template_name, {'slots': slot})
    return render(request, 'main/session.html', {'slots': slot})




#def cancelSession(request):




    # def tutor_detail_view(request,pk):
    #     try:
    #         tutor_id=Book.objects.get(pk=pk)
    #     except Book.DoesNotExist:
    #         raise Http404("Book does not exist")
    #
    #     #book_id=get_object_or_404(Book, pk=pk)
    #
    #     return render(
    #         request,
    #         'main/tutor_detail.html',
    #         context={'tutor_details':tutor_id,}
    #     )
