# **********************OBJ INFO**************************
# Author:Kali Yu
# @Time    : 2018/12/29 18:07
# @Site    : 52ziyu.cn
# @File    : views.py
# @software: PyCharm
# *********************************************************


from django.shortcuts import HttpResponse,render,redirect

from bill.models import BillInfo, Classify

def index(request):
    all_billinfo = BillInfo.objects.all()

    return render(request, 'account.html', {'all_billinfo': all_billinfo})


def add(request):
    if request.method == 'GET':
        all_classify_name = Classify.objects.all()

        return render(request, 'add.html', {'all_classify_name': all_classify_name})

    elif request.method =='POST':
        billinfo = BillInfo()
        type = request.POST.get('type', '')
        classify = request.POST.get('classify', 0)
        date = request.POST.get('date', '')
        money = request.POST.get('money', '')
        ps = request.POST.get('ps', '')

        billinfo.type = type
        billinfo.classify_id = classify
        billinfo.date = date
        billinfo.money = money
        billinfo.ps = ps
        billinfo.save()
        return redirect('/')


def drop(request):
    pass


