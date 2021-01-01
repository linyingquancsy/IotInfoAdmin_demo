from django.shortcuts import render
from django.shortcuts import redirect
from login.models import User
import time
# Create your views here.
def index(request):
    '''
    首页
    '''
    # context = {"temperature": 0.00}
    context = {
        "sensors": {
            "temperature": "Null",
            "humidity": "Null",
            "water": "Null",
            "light": "Null"
        },
        "data": {
            "one": "null"
        }
    }
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'data/index.html', context=context)

def monitoring(request):
    context = {'name': "linying"}
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'data/monitoring.html', context=context)

def Userv(request):
    '''
    用户数据相关
    :param request:
    :return:
    '''
    context = {
        'from': {
            'name': None,
            'sex': None,
            'email': None,
            'c_time': None,
        }}
    user = User.objects.all()
    if not request.session.get('is_login', None):
        return redirect('/login/')
    context['user'] = user

    # 添加数据
    if request.POST:
        context['from']['name'] = request.POST['name']
        context['from']['sex'] = request.POST['sex']
        context['from']['email'] = request.POST['email']
        data = User()
        data.name = request.POST['name']
        if request.POST['sex'] == '男':
            data.sex = 'male'
        else:
            data.sex = 'female'
        data.email = request.POST['email']
        data.c_time = time.ctime
        data.has_confirmed = 1
        data.password = 123456
        data.save()
        # print("已保存", time.ctime, context['from'])
    # 删除数据
    if request.GET and request.GET['pid'] == 'delete':
        name = request.GET['name']
        # User.objects.filter(name=name).delete()
        print("删除成功", name)
    # 修改数据
    if request.GET and request.GET['pid'] == 'set':
        name = request.GET['name']
        pid = request.GET['pid']
        # User.objects.filter(name=name).delete()
        print("修改数据", name, pid)
    return render(request, 'data/User.html', context=context)

def input_data(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    return render(request, 'data/User.html',)

def Device(request):
    context = {'name': "linying"}
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'data/Device.html', context=context)

def testing(request):
    context = {'name': "linying"}
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'data/testing.html', context=context)
