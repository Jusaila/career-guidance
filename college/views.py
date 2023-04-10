from django.shortcuts import render
from college.models import College
# Create your views here.

def colg(request):
    if request.method == "POST":
        obj=College()
        obj.college_name=request.POST.get('collegename')
        obj.college_location=request.POST.get('collegelocation')
        obj.phone=request.POST.get('phone')
        obj.e_mail=request.POST.get('email')
        obj.website=request.POST.get('website')
        obj.course=request.POST.get('Course')
        obj.fee=request.POST.get('Fee')
        obj.save()
    return render(request,'college/college-post.html')


def viewclg(request):
    obj=College.objects.all()
    context={
        'x':obj
    }
    return render(request,'college/college_viewandupdates.html',context)


def update(request,idd):
    ob=College.objects.get(c_id=idd)
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=College.objects.get(c_id=idd)
        obj.college_name = request.POST.get('collegename')
        obj.college_location = request.POST.get('collegelocation')
        obj.phone = request.POST.get('phone')
        obj.e_mail = request.POST.get('email')
        obj.website = request.POST.get('website')
        obj.save()
        return viewclg(request)
    return render(request,'college/update_college.html',context)
