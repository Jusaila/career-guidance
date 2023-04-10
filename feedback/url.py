from django.conf.urls import url
from feedback import views

urlpatterns=[
    url('feed/',views.feed),
    url('viewf/',views.vfeed)
]