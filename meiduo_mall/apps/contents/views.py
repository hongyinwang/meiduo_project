from django import http
from django.shortcuts import render

# Create your views here.


#定义首页视图
from django.views import View


class IndexView(View):

    def get(self,request):

        return render(request,'index.html')