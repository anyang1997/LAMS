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

# 新增学期
def add_term(name, total_weeks, start_date, remark):
    if {'term_name': name} in Term.objects.values('term_name'):
        return False
    else:
        end_date = start_date + datetime.timedelta(days=(total_weeks * 7 - 1))
        Term.objects.create(term_name=name,
                            term_total_weeks=total_weeks,
                            term_start_date=start_date,
                            term_end_date=end_date,
                            term_remark=remark
                            )
        return True


# 删除学期及其下预约记录
def delete_term(name):
    if {'term_name': name} in Term.objects.values('term_name'):
        Book.objects.filter(book_term_name=name).delete()
        Term.objects.filter(term_name=name).delete()
        return True
    else:
        return False


# # 新增预约记录
# def add_book():
