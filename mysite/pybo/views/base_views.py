from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponse

from ..models import Question
from django.db.models import Q
import logging
logger = logging.getLogger('pybo')

def index(request):
    # 3/0
    logger.info("INFO 레벨로 출력.")
    page = request.GET.get('page','1') # page.
    kw = request.GET.get('kw', '') # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()


    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기.
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page':page, 'kw':kw}
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