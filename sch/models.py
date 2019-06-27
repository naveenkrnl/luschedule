from django.db import models
from django.conf import settings
# Create your models here.
class Goal(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    goal_text=models.CharField(max_length=200,null=True,blank=True)
    monday=models.BooleanField(default=False)
    tuesday=models.BooleanField(default=False)
    wednesday=models.BooleanField(default=False)
    thursday=models.BooleanField(default=False)
    friday=models.BooleanField(default=False)
    saturday=models.BooleanField(default=False)
    sunday=models.BooleanField(default=False)
    efficiency=models.CharField(max_length=200,default=0)
    def __str__(self):
        return self.goal_text