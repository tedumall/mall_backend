from django.db import models

from tools.common_tools import convert_time


class UmsRole(models.Model):
    name = models.CharField("名称", max_length=100)
    description = models.CharField("描述", max_length=500, null=True)
    admin_count = models.IntegerField("后台用户数量", default=0)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    status = models.IntegerField("启用状态：0->禁用；1->启用", default=1)
    sort = models.IntegerField("排序", default=0)


# Create your models here.
class UmsAdmin(models.Model):
    username = models.CharField("用户名", max_length=64)
    password = models.CharField("密码", max_length=64)
    icon = models.ImageField("头像", null=True)
    email = models.EmailField("邮箱", null=True)
    nick_name = models.CharField("昵称", max_length=200, default="")
    note = models.TextField("备注", null=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    login_time = models.DateTimeField("最后登录时间", null=True)
    status = models.IntegerField("帐号启用状态：0->禁用；1->启用", default=1)
    role = models.ForeignKey(UmsRole, on_delete=models.CASCADE, null=True)


class UmsMenus(models.Model):
    parent_id = models.BigIntegerField("父级ID", null=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    title = models.CharField("菜单名称", max_length=100)
    level = models.IntegerField("菜单级数", null=True)
    sort = models.IntegerField("菜单排序", null=True)
    name = models.CharField("前端名称", max_length=100, null=True)
    icon = models.CharField("前端图标", max_length=150, null=True)
    hidden = models.IntegerField("前端隐藏", default=0)

    def serize(self):
        menu_dict = {}
        menu_dict["id"] = self.id
        menu_dict["parent_id"] = self.parent_id
        menu_dict["create_time"] = convert_time(self.create_time)
        menu_dict["title"] = self.title
        menu_dict["level"] = self.level
        menu_dict["sort"] = self.sort
        menu_dict["name"] = self.name
        menu_dict["icon"] = self.icon
        menu_dict["hidden"] = self.hidden
        return menu_dict


class UmsRoleMenus(models.Model):
    role_id = models.BigIntegerField("角色id")
    menu_id = models.BigIntegerField("目录id")
