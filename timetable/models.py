from django.db import models
from django.utils import timezone
import datetime
import locale


# 中文编码问题，解决Model中文显示问题
locale.setlocale(locale.LC_CTYPE, 'chinese')


# 学期信息，包括学期名、教学周数、起始日期、备注
class Term(models.Model):

    # 模块名称：学期
    class Meta:
        verbose_name = "学期"
        verbose_name_plural = "学期"

    # 返回学期名
    def __str__(self):
        return self.term_name

    # 学期名
    term_name = models.CharField(verbose_name='学期名', default='XXXX-XXXX学年度第X学期', max_length=50, unique=True)

    # 教学周数
    term_total_weeks = models.IntegerField(verbose_name='教学周数', default=20)

    # 起始日期
    term_start_date = models.DateField(verbose_name='起始日期', default=timezone.localtime)

    # 结束日期
    term_end_date = models.DateField(verbose_name='结束日期', default=timezone.localtime)

    # 备注
    term_remark = models.CharField(verbose_name='备注', default='无', max_length=100)


# 实验室信息，包括实验室名称、照片、位置、描述
class Lab(models.Model):

    # 模块名称：实验室
    class Meta:
        verbose_name = "实验室"
        verbose_name_plural = "实验室"
        ordering = ['lab_num']

    # 显示返回实验室编号、名称
    def __str__(self):
        return self.lab_num + ' ' + self.lab_name

    # 实验室编号
    lab_num = models.CharField(verbose_name='实验室编号', default='XXX', max_length=10, unique=True)

    # 实验室名称
    lab_name = models.CharField(verbose_name='实验室名称', default='XXX实验室', max_length=20)

    # 实验室照片
    lab_pic = models.ImageField(verbose_name='实验室照片', default='default.jpg', upload_to='images/labs')

    # 实验室描述
    lab_desc = models.CharField(verbose_name='实验室描述', default='无', max_length=100)


# 教学周信息，放置学期、第几周对应时间
class Week(models.Model):

    # 模块名称：学期
    class Meta:
        verbose_name = "教学周"
        verbose_name_plural = "教学周"
        ordering = ['week_term']

    # 显示返回学期名、第几周
    def __str__(self):
        return str(self.week_term) + ' ' + str(self.week_ord)

    # 学期名
    week_term = models.ForeignKey(verbose_name='学期名', to='Term', to_field='term_name', on_delete=False)

    # 第几周
    week_ord = models.IntegerField(verbose_name='第几周', default='0')

    # 起始日期
    week_start_date = models.DateField(verbose_name='起始日期', default=timezone.localtime)

    # 结束日期
    week_end_date = models.DateField(verbose_name='结束日期', default=timezone.localtime)

    # 备注
    week_remark = models.CharField(verbose_name='备注', default='无', max_length=100)


# 预约记录
class Book(models.Model):

    # 模块名称：预约
    class Meta:
        verbose_name = "预约"
        verbose_name_plural = "预约"

    # 前端显示
    def __str__(self):
        return datetime.date.strftime(self.book_date, '%Y年%m月%d日  ')\
               + self.book_start_time.strftime('%H:%M -')\
               + self.book_end_time.strftime(' %H:%M  ') \
               + self.book_order + '  '\
               + self.book_subject

    # 学期
    book_term_name = models.ForeignKey(verbose_name='学期', default='未知学期', to='Term', to_field='term_name',
                                       on_delete=False)

    # 预约人信息
    book_order = models.CharField(verbose_name='预约人', default='未知预约人', max_length=10)

    # 课程名称
    book_subject = models.CharField(verbose_name='课程名称', default='XX课程', max_length=10)

    # 实验室编号
    book_lab_num = models.ForeignKey(verbose_name='实验室编号', to='Lab', to_field='lab_num', on_delete=False)

    # 预约日期
    book_date = models.DateField(verbose_name='预约日期', default=timezone.localtime)

    # 开始时间
    book_start_time = models.TimeField(verbose_name='开始时间', default=timezone.localtime)

    # 结束时间
    book_end_time = models.TimeField(verbose_name='结束时间', default=timezone.localtime)

    # 备注
    book_remark = models.CharField(verbose_name='备注', default='无', max_length=100)
