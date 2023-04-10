from django.conf.urls import url
from course import views

urlpatterns=[
    url('course/',views.course),
    url('vcrs/',views.vcourse),
    url('vup/', views.vcrs),
    url('new/(?P<idd>\w+)',views.update,name='update'),
]