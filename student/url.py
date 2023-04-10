from django.conf.urls import url
from student import views

urlpatterns = [
    url('student/', views.register),
    url('vprof/',views.vstud)

]