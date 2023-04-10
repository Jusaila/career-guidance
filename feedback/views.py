from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.

def feed(request):
    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'feedback/feedback.html')




def vfeed(request):
    obj=Feedback.objects.all()
    context={
        'bb': obj
    }
    return render(request,'feedback/viewfeedback.html',context)