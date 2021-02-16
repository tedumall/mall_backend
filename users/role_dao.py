import datetime
import json

from django.core import serializers

from users.models import *


class RoleDao:
    @staticmethod
    def getMenuList(adminId):
        role = RoleDao.get_roles(adminId)

        role_menus_list = UmsRoleMenus.objects.filter(role_id=role.id).values("menu_id")
        query_list = UmsMenus.objects.filter(id__in=role_menus_list)
        menus_list = []
        for q in query_list:
            menus_list.append(q.serize())
        return menus_list

    @staticmethod
    def get_roles(adminId):
        user = UmsAdmin.objects.get(id=adminId)
        role = user.role
        return role

    @staticmethod
    def get_all():
        roles = UmsRole.objects.all()
        res_list = []
        for role in roles:
            res_list.append(role.serize())

        return res_list
