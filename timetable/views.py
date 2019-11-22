from django.shortcuts import *
from django.contrib import auth
from django.http import *
import datetime
import time

from .models import *

# Create your views here.


def index(request):

    context = {'datetime': datetime.datetime.now()}
    current_monday = get_current_weekday()
    current_sunday = current_monday + datetime.timedelta(days=6)
    context.update({'current_monday': current_monday})
    [current_term, current_week] = get_current_term(current_monday)
    context.update({'current_term': current_term})
    context.update({'current_week': current_week})
    lab_num = Lab.objects.get(lab_num='501').lab_num
    context.update({'lab_num': lab_num})
    lab_name = Lab.objects.get(lab_num='501').lab_name
    context.update({'lab_name': lab_name})
    for i in range(1, 8):
        day = 'date_' + str(i)
        day_week = current_monday + datetime.timedelta(days=(i-1))
        context.update({day: day_week})
    book_list = Book.objects.filter(book_date__gte=current_monday).filter(book_date__lte=current_sunday)
    
    # 获取预约
    
    for i in range(1, 8):
        book_date = 'book_date_' + str(i)
        date_week = current_monday + datetime.timedelta(days=(i-1))
        book = book_list.filter(book_date=date_week).filter(book_lab_num=lab_num).all()
        context.update({book_date: book})


    # 查询模块

    # 获取学期
    term_list = Term.objects.all()
    context.update({'term_list': term_list})


    # 获取实验室
    lab_list = Lab.objects.all()
    context.update({'lab_list': lab_list})



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
    # init_week()
    context = {'datetime': datetime.datetime.now()}
    if request.user.is_superuser:
        books = Book.objects.all()
    elif request.user.is_authenticated:
        books = Book.objects.filter(book_order=request.user.first_name).all()
    else:
        books = None
    context.update({'books': books})
    return render(request, 'manage.html', context)


def inquire(request):
    context = {'datetime': datetime.datetime.now()}
    if request.method == 'GET':
        # 获取ajax的json对象
        current_term_id = request.GET.get('term_name')
        lab_num_id = request.GET.get('lab_num')
        week_ord_id = request.GET.get('week_ord')

        # 读取数据库
        current_monday = Week.objects.get(id=week_ord_id).week_start_date
        current_sunday = current_monday + datetime.timedelta(days=6)

        context.update({'current_monday': current_monday})

        current_term = Term.objects.get(id=current_term_id).term_name
        current_week = Week.objects.get(id=week_ord_id).week_ord

        context.update({'current_term': current_term})
        context.update({'current_week': current_week})

        lab_num = Lab.objects.get(id=lab_num_id).lab_num
        lab_name = Lab.objects.get(id=lab_num_id).lab_name

        context.update({'lab_num': lab_num})
        context.update({'lab_name': lab_name})

        for i in range(1, 8):
            day = 'date_' + str(i)
            day_week = current_monday + datetime.timedelta(days=(i - 1))
            context.update({day: day_week})
        book_list = Book.objects.filter(book_date__gte=current_monday).filter(book_date__lte=current_sunday)

        # 获取预约

        for i in range(1, 8):
            book_date = 'book_date_' + str(i)
            date_week = current_monday + datetime.timedelta(days=(i - 1))
            book = book_list.filter(book_date=date_week).filter(book_lab_num=lab_num).all()
            context.update({book_date: book})

        # 查询模块

        # 获取学期
        term_list = Term.objects.all()
        context.update({'term_list': term_list})

        # 获取实验室
        lab_list = Lab.objects.all()
        context.update({'lab_list': lab_list})

        return render(request, 'index.html', context)

def get_week_ord(request):
    if request.is_ajax():
        term_id = request.GET.get('term_name')
        name = Term.objects.get(id=term_id).term_name
        week_ord_list = Week.objects.filter(week_term_name=name)
        context = {}
        for week in week_ord_list:
            context.update({week.week_ord: week.id})
        return JsonResponse(context)


def book(request):
    if request.method == 'POST':
        term_name = request.POST.get('term_name')
        order = request.POST.get('order_name')
        lab_num = request.POST.get('lab_num')
        subject = request.POST.get('subject')
        date_t = request.POST.get('book_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        remark = request.POST.get('remark')

        date = str(date_t).replace('年', '-').replace('月', '-').replace('日', '')
        if add_book(term_name=term_name,
                    order=order,
                    subject=subject,
                    lab_num=lab_num,
                    date=date,
                    start_time=start_time,
                    end_time=end_time,
                    remark=remark):
            print("ADD BOOK SUCCESS!")
        else:
            print("FAILED")
    return redirect('/manage', {'script': "alert", 'wrong': '账号错误'})


def delete(request):
    if request.method == 'POST':
        for id in request.POST:
            if id == 'csrfmiddlewaretoken':
                print('CSRF TOKEN:')
            else:
                Book.objects.filter(id=id).delete()
    return redirect('/manage')




############################################################################

# 常用功能
# 获得本周周一
def get_current_weekday():
    monday = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while monday.weekday() != 0:
        monday -= one_day
    return monday

# 定位本学期
def get_current_term(current_day):
    return [
        Week.objects.get(week_start_date__lte=current_day, week_end_date__gte=current_day).week_term_name,
        Week.objects.get(week_start_date__lte=current_day, week_end_date__gte=current_day).week_ord,
    ]
            





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

    book_list = Book.objects.filter(book_term_name=term_name).filter(book_lab_num=lab_num).filter(book_date=date).all()

    s = datetime.datetime.strptime(start_time, '%H:%M')
    e = datetime.datetime.strptime(end_time, '%H:%M')

    # for book in book_list:
    #     print(book.book_start_time)
    #     if s < book.book_start_time < e or\
    #             s < book.book_end_time < e:
    #         return False

    term = Term.objects.get(term_name=term_name)
    lab = Lab.objects.get(lab_num=lab_num)
    Book.objects.create(book_term_name=term,
                        book_order=order,
                        book_subject=subject,
                        book_lab_num=lab,
                        book_date=date,
                        book_start_time=start_time,
                        book_end_time=end_time,
                        book_remark=remark)
    return True



# 根据学期信息生成教学周表
def init_week():
    term_list = Term.objects.all()
    Week.objects.all().delete()
    for term in term_list:
        total_weeks = term.term_total_weeks
        for i in range(1, total_weeks+1):
            start_date = term.term_start_date + datetime.timedelta(days=((i-1)*7))
            term_name = Term.objects.get(pk=term.id)
            Week.objects.create(week_term_name=term_name,
                                week_ord=i,
                                week_start_date=start_date,
                                week_end_date=start_date+datetime.timedelta(days=6)
                                )
            print(str(total_weeks) + ' + ' + str(i))
    return True


