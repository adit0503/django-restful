from django.db import models

# Create your models here.
class Game(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120, default='')
    release_date = models.DateTimeField()
    esrb_rating = models.CharField(max_length=1250, default='')
    played_once = models.BooleanField(default=False)
    payed_times = models.IntegerField(default=0)

    class Meta:
        ordering = ['name',]
