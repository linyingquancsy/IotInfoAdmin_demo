from django.shortcuts import render
from django.shortcuts import redirect
from login.models import User
from api.models import Sensor
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
    sen = Sensor.objects.all()
    # print(sen.get('tem'))
    for i in sen:
        context['sensors']['temperature'] = i.tem
        context['sensors']['humidity'] = i.hum
        context['sensors']['water'] = i.water
        context['sensors']['light'] = i.light
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'data/index.html', context=context)

# def monitoring(request):
#     context = {'name': "linying"}
#     if not request.session.get('is_login', None):
#         return redirect('/login/')
#     return render(request, 'data/monitoring.html', context=context)

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
        # print("删除成功", name)
    # 修改数据
    if request.GET and request.GET['pid'] == 'set':
        name = request.GET['name']
        pid = request.GET['pid']
        # print("修改数据", name, pid)
    return render(request, 'data/User.html', context=context)

# from django.http import HttpResponse
# from django.views.generic import View
# from data.forms import MessageForm
# class set_data(View):
#     def get(self, request):
#         form = MessageForm()
#         return render(request, 'myhtml/set_data.html', {'form': form})
#     def post(self, request):
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             email = form.cleaned_data.get('email')
#             # print(title, email, request.POST.get['name'])
#             print(title, email)
#             return HttpResponse("success")
#         else:
#             print(form.errors)
#             return HttpResponse('fail')

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
