import json

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core import serializers
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from  django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    page = request.GET.get('page','1') # page.
    question_list = Question.objects.order_by('-create_date')

    #old
    # context = {'question_list': question_list}

    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기.
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def jsontest(request):
    question_list = Question.objects.order_by('-create_date')[:3]
    # question_list = Question.objects.order_by('-create_date')
    # context = {'question_list': question_list}
    question_list = list(question_list.values('subject', 'content', 'create_date'))
    # for question in question_list:
    #     question['create_date']=str(question['create_date'])
    question_list = serializers.serialize('json', question_list, fields=('subject', 'content', 'create_date'))
    return HttpResponse(json.dumps(question_list), content_type="application/json")

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # c1
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    # c2
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()

    # c3
    # use AnswerForm
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장.
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user # author 속성에 로그인 계정 저장.
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')