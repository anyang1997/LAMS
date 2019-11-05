from django.db import models

# Create your models here.


# 实验室信息，包括实验室房间号、照片、位置、描述
class Labs(models.Model):

    # 模块名称：实验室管理
    class Meta:
        verbose_name = "实验室管理"
        verbose_name_plural = "实验室管理"
        ordering = ['num']

    # 显示返回实验室编号
    def __str__(self):
        return self.num

    # 实验室编号
    num = models.CharField(verbose_name='实验室编号', max_length=10)

    # 实验室位置
    addr = models.CharField(verbose_name='实验室位置', max_length=10)

    # 实验室照片
    pic = models.ImageField(verbose_name='实验室照片', upload_to='images')

    # 实验室描述
    desc = models.CharField(verbose_name='实验室描述', max_length=50)


# 学期信息，放置学期第几周对应时间
class Term(models.Model):

    # 模块名称：学期管理
    class Meta:
        verbose_name = "学期管理"
        verbose_name_plural = "学期管理"
        ordering = ['week']

    # 显示返回第几周
    def __str__(self):
        return self.week

    # 第几周
    week = models.CharField(verbose_name='第几周', max_length=10)

    # 起始日期
    start = models.DateField(verbose_name='起始日期')

    # 结束日期
    end = models.DateField(verbose_name='结束日期')


# Appointment模块用于存放预约信息
class Appointment(models.Model):

    # 预约模块
    class Meta:
        verbose_name = "预约管理"
        verbose_name_plural = "预约管理"

    # 前端显示
    def __str__(self):
        pass

    # 预约人信息
    order = models.CharField(verbose_name='预约人', max_length=10)

    # 课程名称
    subject = models.CharField(verbose_name='课程名称', max_length=10)

    # 实验室编号
    lab = models.CharField(verbose_name='实验室编号', max_length=10)

    # 预约日期
    day = models.DateField(verbose_name='预约日期')

    # 开始时间
    start = models.TimeField(verbose_name='开始时间')

    # 结束时间
    end = models.TimeField(verbose_name='结束时间')

    # 备注
    remark = models.CharField(verbose_name='备注', max_length=50)
