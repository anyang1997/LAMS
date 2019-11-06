from django.shortcuts import *
from django.contrib import auth
import datetime
from .models import *

# Create your views here.


def index(request):
    a = Book.objects
    # init_var(total_weeks='20', term_name='2019-2020第一学期',
    #          first_day='2019-10-28')
    # init_term()
    return render(request, 'hello.html', {'a': a})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # 认证
        username = auth.authenticate(username=user, password=pwd)
        if username:
            auth.login(request, user)
        return redirect('/index/')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login/')


def order(request):
    return


def preview(request):
    return


def table(request):
    return


def config(request):
    return


# 相关数据库操作

# # 全局变量初始化
# def init_var(total_weeks, term_name, first_day):
#
#     # 初始化教学周总周数
#     if {'name': 'TOTAL_WEEKS'} in Variable.objects.values('name'):
#         Variable.objects.filter(name='TOTAL_WEEKS').update(value=total_weeks)
#     else:
#         Variable.objects.create(name='TOTAL_WEEKS', value=total_weeks)
#
#     # 初始化学期名
#     if {'name': 'TERM_NAME'} in Variable.objects.values('name'):
#         Variable.objects.filter(name='TERM_NAME').update(value=term_name)
#     else:
#         Variable.objects.create(name='TERM_NAME', value=term_name)
#
#     # 初始化第一周的第一天
#     if {'name': 'FIRST_DAY'} in Variable.objects.values('name'):
#         Variable.objects.filter(name='FIRST_DAY').update(value=first_day)
#     else:
#         Variable.objects.create(name='FIRST_DAY', value=first_day)
#
#
# # 初始化教学周
# def init_term():
#     total_weeks = int(Variable.objects.get(name='TOTAL_WEEKS').value)
#     first_day = datetime.datetime.strptime(Variable.objects.get(name='FIRST_DAY').value, '%Y-%m-%d').date()
#
#     # 删除原有的教学周
#     Term.objects.all().delete()
#
#     # 重新生成教学周
#     for i in range(1, total_weeks+1):
#         week = '第' + str(i) + '周'
#         start = first_day + datetime.timedelta(days=(i-1)*7)
#         end = start + datetime.timedelta(days=6)
#         Term.objects.create(week=week, start=start, end=end)
#
