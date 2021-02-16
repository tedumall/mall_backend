from django.contrib.auth.admin import UserAdmin
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tools.login_dec import login_check
from tools.response_tool import ResponseUtil
from users.role_dao import *


@login_check
def info(request):
    user = request.myuser
    username = user.username
    icon = str(user.icon)

    #     {"id": 1, "parentId": 0, "createTime": "2020-02-02T06:50:36.000+00:00", "title": "商品", "level": 0, "sort": 0,
    #      "name": "pms", "icon": "product", "hidden": 0},

    menuslist = getMenuList(user.id)
    res = {"username": username, "icon": icon, "roles": [get_roles(user.id).name], "menus": menuslist}

    return ResponseUtil.success(res)
