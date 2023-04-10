from django.db import models

# Create your models here.
class College(models.Model):
    c_id = models.AutoField(db_column='c-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    college_name = models.CharField(max_length=100)
    college_location = models.CharField(max_length=100)
    phone = models.IntegerField()
    e_mail = models.CharField(db_column='e-mail', max_length=100)  # Field renamed to remove unsuitable characters.
    website = models.CharField(max_length=500)


    class Meta:
        managed = False
        db_table = 'college'


