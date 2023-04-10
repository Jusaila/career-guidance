from django.db import models

# Create your models here.
class Login(models.Model):
    l_id = models.AutoField(db_column='l-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    u_id = models.IntegerField()
    # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'login'

