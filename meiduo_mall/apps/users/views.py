import re
from django import http
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
# Create your views here.
from apps.users.models import User

from django.http import HttpResponse
#导包
import logging
#创建日志实例,
logger = logging.getLogger('django')

#定义注册类视图
class RegisterView(View):
    #类视图里面的请求函数是以请求方法命名的
    def get(self,request):

        return render(request,'register.html')

    def post(self,request):
        #接受请求数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        #是否同义协议
        allow = request.POST.get('allow')

        #1判断参数是否齐全
        if not all([username,password,password2,mobile,allow]):
            #如果不齐全,则返回失败的相应请求
            return http.HttpResponseBadRequest("参数不齐全")
        # 判断用户名是否是5-20个字符
        if not re.match(r'^[a-zA-Z0-9]{5,20}$',username):
            return http.HttpResponseBadRequest("用户名不在范围内")
        # 判断密码是否是8-20个数字
        if not re.match(r'^[a-zA-Z0-9]{8,20}$',password):
            return http.HttpResponseBadRequest("密码不在范围内")
        #判断两次密码是否一直
        if password != password2:
            return http.HttpResponseBadRequest("两次密码不一致")
            # 判断手机号是否合法
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseBadRequest('请输入正确的手机号码')
        #判断是否同意协议
        if allow != 'on':
            return http.HttpResponseBadRequest('不同意协议')

        #保存注册数据
        #预处理异常
        try:
            user = User.objects.create_user(
                username = username,
                password = password,
                mobile = mobile
            )
        except Exception as e:
            logger.error(e)
            return render(request,'register.html',context={'register_errmsg':'注册失败'})
        #状态保持
        login(request,user)
        #跳转首页
        # 对于未指明namespace的，reverse(路由name)
        # 对于指明namespace的，reverse(命名空间namespace: 路由name)
        return redirect(reverse("contents:indexview"))
        # return http.HttpResponse("ok")

#判断username是否重复
class UsernameCountView(View):

    def get(self,request,username):

        #u02:用户名查询
        count = User.objects.filter(username=username).count()
        #u03:返回响应对象（JsonResponse可以把数据转化成json字符串的形式）
        return http.JsonResponse({'count':count})