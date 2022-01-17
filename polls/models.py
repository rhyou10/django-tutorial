import datetime
from msilib.schema import Class
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date puublished')

    def __str__(self) :
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #외래키 question 참조 CASCADE는 위의 qustion이 사라지면 여기도 사라진다.
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

    def __str__(self) :
        return self.choice_text
# Create your models here.
