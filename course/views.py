from django.shortcuts import render
from sklearn.metrics import pairwise_distances_argmin

from course.models import Course
from college.models import College
# Create your views here.

def course(request):
    obv=College.objects.all()
    context={
        'hh':obv
    }
    if request.method=='POST':
        obj=Course()
        obj.c_id=request.POST.get('clg')
        obj.course=request.POST.get('crs')
        obj.course_details=request.POST.get('course_details')
        obj.save()
    return render(request,'course/course.html',context)




def vcourse(request):
    if request.method=="POST":
        vv=request.POST.get('name')
        obj=Course.objects.filter(course__istartswith=vv)
        # obj=Course.objects.all()
        context={
            'a':obj
        }
    # return render(request,'course/viewcourse.html',context)
    else:
        obj=Course.objects.all()
        context={
            'a':obj
        }
    return render(request,'course/viewcourse.html',context)

def vcrs(request):
    obj=Course.objects.all()
    context={
        'a':obj
    }
    return render(request,'course/vup.html',context)


def update(request,idd):
    ob=College.objects.get(c_id=idd)
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=Course()
        obj=Course.objects.get(course_id=idd)
        obj.course = request.POST.get('crs')
        obj.course_details = request.POST.get('course_details')
        obj.save()
        return vcrs(request)
    return render(request,'course/updateourse.html',context)