
from django.conf.urls import url,include
#导入视图函数
from . import views

urlpatterns = [
    #users
    url(r'^indexview/$',views.IndexView.as_view(),name='indexview'),

]

