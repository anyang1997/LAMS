# Generated by Django 2.2.5 on 2019-11-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20191106_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_term_name',
            field=models.ForeignKey(default='未知', on_delete=False, to='timetable.Term', to_field='term_name', verbose_name='学期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_subject',
            field=models.CharField(default='XX课程', max_length=10, verbose_name='课程名称'),
        ),
    ]