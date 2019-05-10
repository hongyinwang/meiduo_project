from tabnanny import verbose

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#自定义模型类
class User(AbstractUser):

    #创建字段
    mobile = models.CharField(max_length=20,unique=True,verbose_name='手机号')

    #重命名表名
    class Meta:
        db_table = 'db_table'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    #定义一个显示字段的方法
    def __str__(self):
        return self.username #username为继承类中表字段的用户名

#这里面需要注意迁移之后就保存到数据库中了