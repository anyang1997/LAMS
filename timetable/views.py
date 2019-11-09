from django.shortcuts import *
from django.contrib import auth
import datetime
from .models import *

# Create your views here.


def index(request):
    context = {'datetime': datetime.datetime.now()}
    current_monday = get_current_week()
    for i in range(1, 8):
        day = 'date_' + str(i)
        day_week = current_monday + datetime.timedelta(days=(i-1))
        context.update({day: day_week})
    print(context)
    return render(request, 'index.html', context)


def login(request):

    # 获取POST的用户名和密码
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 认证
        username = auth.authenticate(username=username, password=password)
        if username:
            auth.login(request, username)
        return redirect('/')

    return render(request, 'index.html')


def logout(request):

    # 直接登出，重定向到登录界面
    auth.logout(request)
    return redirect('/')

def changepassword(request):

    return

def about(request):
    return


def manage(request):
    context = {'datetime': datetime.datetime.now()}
    books = Book.objects.all()
    context.update({'books': books})
    return render(request, 'manage.html', context)


# 常用功能
def get_current_week():
    monday = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while monday.weekday() != 0:
        monday -= one_day
    return monday







# 相关数据库操作

# 新增学期
def add_term(term_name, total_weeks, start_date, remark):
    if {'term_name': term_name} in Term.objects.values('term_name'):
        return False
    else:
        end_date = start_date + datetime.timedelta(days=(total_weeks * 7 - 1))
        Term.objects.create(term_name=term_name,
                            term_total_weeks=total_weeks,
                            term_start_date=start_date,
                            term_end_date=end_date,
                            term_remark=remark
                            )
        return True


# 删除学期、教学周及其下预约记录
def delete_term(term_name):
    if {'term_name': term_name} in Term.objects.values('term_name'):
        Book.objects.filter(book_term_name=term_name).delete()
        Week.objects.filter(week_term_name=term_name).delete()
        Term.objects.filter(term_name=term_name).delete()
        return True
    else:
        return False


# 新增预约记录
def add_book(term_name, order, subject, lab_num, date, start_time, end_time, remark):
    book_list = Book.objects.filter(book_term_name=term_name, book_lab_num=lab_num)
    for book in book_list:
        if book_list.book_start_time in range(start_time, end_time)\
                or book_list.book_end_time in range(start_time, end_time):
            return False
        else:
            Book.objects.create(book_term_name=term_name,
                                book_order=order,
                                book_subject=subject,
                                book_lab_num=lab_num,
                                book_date=date,
                                book_start_time=start_time,
                                book_end_time=end_time,
                                book_remark=remark)
            return True


# 删除预约记录
def delete_book(book_id, order):
    return