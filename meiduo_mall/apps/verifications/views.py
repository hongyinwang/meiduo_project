from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View


class ImageCodeView(View):
    #获取参数
    #通过get方式获取uuid,这里面的uuid适合之前的校验参数的uuid相互照应
    def get(self,request,uuid):
        #生成图片验证码内容和二进制图片
        from libs.captcha.captcha import captcha

        text,image = captcha.generate_captcha()
        #链接数据库
        from django_redis import get_redis_connection
        redis_conn = get_redis_connection("code")
        #保存数据库，设置时效
        #这里面到为什么key==uuit valid==text 是因为生成的图片验证码内容
        #是通过uuid来获取到的
        redis_conn.setex('img_%s'%uuid,300,text)
        #把图片返回个浏览器
        return http.HttpResponse(image,content_type='image.jpeg')