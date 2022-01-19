# Django 튜토리얼 및 실습
- 2022-01-07 시작



## 2022-01-07

### Djnago 설치

- 새로운 프로젝트 폴더 생성
- 가상환경 설치 생성 실행 django 설치

```
pip install virtualenv #설치
virtualenv env이름 #생성
env이름\Scripts\activate.bat #실행 가상환경종료 deactivate
pip install Django #가상환경에 django 설치
py -m jango
```



### Django 프로젝트 만들기, 실행, 앱생성

```
django -admin startproject mysite

py mange.py runserver

py manage.py startapp polls #polls앱생성
```



### 데이터베이스 설정

```
python manage.py migrate ## setting.py에 있는 데이터 베이스에 따라 테이블 생성

## 앱이름/models.py
## Question, Choice 
from django.db import models 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
## 프로젝트의 앱 포합할시
# 프로젝트명(mysite)/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ] #추가해야한다.
```



### API 사용

```
python manage.py shell # 셸 호출
from polls.models import Choice, Question #모델 호출
from django.utils import timezone #시간
q = Question(question_text="What's new?", pub_date=timezone.now()) # 데이터 입력
q.save()
q.id #--> 1
q.question_text
q.pub_date
q.question_text = "hi" #변경가능
q.save
```

