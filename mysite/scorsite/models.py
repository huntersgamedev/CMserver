from django.db import models
from django.contrib.auth.models import User
import operator





# Create your models here.


class PostUserScore(models.Model):
    UserName = models.CharField(max_length=100,default='xxxxxxxx')
    Score = models.CharField(max_length=100,default =0)
    FirstName = models.CharField(max_length=100, default='stanley')
    LastName = models.CharField(max_length=100, default=' charlston')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
   
    #ordered=sorted(LeaderBoard,Key=operator.attrgetter('Score'))
    
    class Meta:
        ordering=('-Score',)

    def __str__(self):
        return self.FirstName + ' - ' + self.LastName + ' - ' + self.Score

class UserSaveFile(models.Model):
    UserName = models.CharField(max_length=100,default='xxxxxxxx')

    CharHead = models.CharField(max_length=100,default =0)
    CharBody = models.CharField(max_length=100,default =0)
    
    Tutorial = models.CharField(max_length=100,default =0)
    
    CooksScore = models.CharField(max_length=100,default =0)
    CooksQuiz = models.CharField(max_length=100,default =0)
    
    HomesScore = models.CharField(max_length=100,default =0)
    HomesQuiz = models.CharField(max_length=100,default =0)
    
    ToysScore = models.CharField(max_length=100,default =0)
    ToysQuiz = models.CharField(max_length=100,default =0)
    
  
