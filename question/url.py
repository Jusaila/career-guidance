from django.conf.urls import url
from question import views

urlpatterns=[
    url('post/',views.post),
    url('view/',views.prediction)
]
