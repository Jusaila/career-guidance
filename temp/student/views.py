from django.shortcuts import render
from student.models import Register
from login.models import Login
# Create your views here.
def register(request):
    if request.method == 'POST':
        obj=Register()
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.phone=request.POST.get('phone')
        obj.e_mail=request.POST.get('email')
        obj.gender=request.POST.get('gender')
        obj.save()

        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.type = "student"
        ob.u_id = obj. s_id
        ob.save()
    return render(request, 'student/register.html')


def vstud(request):
    obj=Register.objects.all()
    context={
        'kk':obj
    }
    return render(request,'student/vprofilestudent.html',context)


