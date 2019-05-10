
from django.conf.urls import url,include
#导入视图函数
from . import views

urlpatterns = [
    #users
    url(r'^register/$',views.RegisterView.as_view(),name='register'),

]

