from django.db import models

# Create your models here.
class Register(models.Model):
    s_id = models.AutoField(db_column='s-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    e_mail = models.CharField(db_column='e-mail', max_length=50)  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'register'

