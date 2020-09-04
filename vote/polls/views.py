from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from Captcha import Captcha
from polls.models import Subject, Teacher
from utils import gen_random_code

# Create your views here.


def show_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'teachers.html', {'subject': subject, 'teachers': teachers})
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


def prise_or_criticize(request):
    try:
        tno = int(request.GET.get('tno'))
        teacher = Teacher.objects.get(no=tno)
        if request.path.startswith('/praise'):
            teacher.good_count += 1
            count = teacher.good_count
        else:
            teacher.bad_count += 1
            count = teacher.bad_count
        teacher.save()
        data = {'code': 20000, 'mesg': '操作成功', 'count': count}
    except (ValueError, Teacher.DoesNotExist):
        data = {'code': 20001, 'mesg': '操作失败'}
    return JsonResponse(data)


def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    return render(request, 'login.html', {'hint': hint})


def get_captcha(request: HttpRequest) -> HttpResponse:
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')
