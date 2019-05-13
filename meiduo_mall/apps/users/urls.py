
from django.conf.urls import url,include
#导入视图函数
from . import views

urlpatterns = [
    #users
    url(r'^register/$',views.RegisterView.as_view(),name='register'),
    #u01:校验
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/$',views.UsernameCountView.as_view(),name='username'),

]

