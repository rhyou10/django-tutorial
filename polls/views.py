from re import template
from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    #1
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    #2
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list' : latest_question_list}
    #return HttpResponse(template.render(context, request))

    #3 render 사용
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    

# Create your views here.

def detail(request, question_id):
    #1
    #return HttpResponse("you're looking at question %s." % question_id)

    #2 404error 발생
    #try:
    #   question = Question.objects.get(pk=question_id)

    #except Question.DoesNotExist:
    #    raise Http404('Question does not exist')
    #return render(request, 'polls/detail.html',{'question' : question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})



def results(request, question_id):
    response = "you're lokking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s." % question_id)