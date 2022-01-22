from re import template

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse

#def index(request):
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
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# Create your views here.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#def detail(request, question_id):
    #1
    #return HttpResponse("you're looking at question %s." % question_id)

    #2 404error 발생
    #try:
    #   question = Question.objects.get(pk=question_id)

    #except Question.DoesNotExist:
    #    raise Http404('Question does not exist')
    #return render(request, 'polls/detail.html',{'question' : question})
 #   question = get_object_or_404(Question, pk=question_id)
 #  return render(request, 'polls/detail.html', {'question':question})



#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExitst):
        #돌려보낸다 
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "you didn't select a choice.",
        })

    else:
        selected_choice.votes +=1
        selected_choice.save()
        # 항상 저장해야지 서버에 들어가는거 인지해야한다.

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))