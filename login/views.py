from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('pswrd')
        obj=Login.objects.filter(username=uname,password=passw)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=='admin':
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/admin/')
            if tp=='student':
                    request.session["uid"]=uid
                    return HttpResponseRedirect('/temp/student/')
        objlist="Username or password incorrect"
        context ={
            'msg':objlist
        }
        return render(request,'login/login.html',context)
    return render(request,'login/login.html')