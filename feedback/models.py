from django.db import models

# Create your models here.
class Feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=25)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedback'

