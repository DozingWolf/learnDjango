from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    return HttpResponse('Hello world! this is my first django framework page!')
def detail(request,question_id):
    return HttpResponse('U R looking at question %s.' % question_id)
def results(request,question_id):
    response = 'U R looking at the results of question %s'
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse('U R voting on question %s' % question_id)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_test for q in latest_question_list])
    return HttpResponse(output)
