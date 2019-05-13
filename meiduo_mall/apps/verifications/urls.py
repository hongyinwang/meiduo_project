
from django.conf.urls import url,include
#导入视图函数
from . import views

urlpatterns = [
    #imagecode
    url(r'^image_codes/(?P<uuid>[\w-]+)/',views.ImageCodeView.as_view(),name='imagecodes'),

]

