from django.db import models
from college.models import College
# Create your models here.


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    # c_id = models.IntegerField()
    c=models.ForeignKey(College,on_delete=models.CASCADE)
    course = models.CharField(max_length=25)
    course_details = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'course'

