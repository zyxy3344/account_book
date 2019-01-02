# **********************OBJ INFO**************************
# Author:Kali Yu
# @Time    : 2019/1/1 20:36
# @Site    : 52ziyu.cn
# @File    : models.py
# @software: PyCharm
# *********************************************************

from django.db import models

from datetime import datetime

class Classify(models.Model):
    name = models.CharField(max_length=32, verbose_name='分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'

class BillInfo(models.Model):
    type = models.CharField(max_length=32, verbose_name='类型')
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE, verbose_name='分类')
    date = models.DateTimeField(default=datetime.now() ,verbose_name='日期')
    money = models.IntegerField(null=True, default=0 ,verbose_name='金额(元)')
    ps = models.CharField(max_length=32, verbose_name='备注')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = '账单信息'
