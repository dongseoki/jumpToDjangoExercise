from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponse

from ..models import Question


def index(request):
    page = request.GET.get('page','1') # page.
    question_list = Question.objects.order_by('-create_date')

    #old
    # context = {'question_list': question_list}

    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기.
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

# def jsontest(request):
#     question_list = Question.objects.order_by('-create_date')[:3]
#     # question_list = Question.objects.order_by('-create_date')
#     # context = {'question_list': question_list}
#     question_list = list(question_list.values('subject', 'content', 'create_date'))
#     # for question in question_list:
#     #     question['create_date']=str(question['create_date'])
#     question_list = serializers.serialize('json', question_list, fields=('subject', 'content', 'create_date'))
#     return HttpResponse(json.dumps(question_list), content_type="application/json")

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)


def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')