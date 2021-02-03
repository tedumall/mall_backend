from django.db import models

# Create your models here.
class UmsAdmin(models.Model):
    username = models.CharField("用户名", max_length=64)
    password = models.CharField("密码", max_length=64)
    icon = models.ImageField("头像", null=True)
    email = models.EmailField("邮箱", null=True)
    nick_name = models.CharField("昵称", max_length=200, default="")
    note = models.TextField("备注", null=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    login_time = models.DateTimeField("最后登录时间",null=True)
    status = models.IntegerField("帐号启用状态：0->禁用；1->启用", default=1)
