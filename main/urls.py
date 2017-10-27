from django.conf.urls import url

from django.views.generic.detail import DetailView
from main import views


app_name = 'main'

urlpatterns=[
    url(r'^$',views.IndexView.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^session/$', views.bookSession, name='session'),
    url(r'^tutors$',views.TutorListView.as_view(), name = 'tutor-list'),
    url(r'^tutors/(?P<pk>\d+)$', views.TutorDetailView.as_view(), name='tutor-detail'),
]
