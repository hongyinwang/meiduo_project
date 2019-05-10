from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
#导包
from jinja2 import Environment

# 1.Jinja2创建模板引擎环境配置文件
def jinja2_environment(**options):
    #实例化对象
    env = Environment(**options)
    #声明更新环境变量
    env.globals.update({
        'static':staticfiles_storage.url,
        'url':reverse,
    })
    return env
