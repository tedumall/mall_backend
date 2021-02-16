from django.contrib.auth.admin import UserAdmin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from tools.login_dec import login_check
from tools.response_tool import ResponseUtil
from users.role_dao import *
from users.user_dao import UserDao


@login_check
def info(request):
    user = request.myuser
    username = user.username
    icon = str(user.icon)

    #     {"id": 1, "parentId": 0, "createTime": "2020-02-02T06:50:36.000+00:00", "title": "商品", "level": 0, "sort": 0,
    #      "name": "pms", "icon": "product", "hidden": 0},

    menuslist = RoleDao.getMenuList(user.id)
    res = {"username": username, "icon": icon, "roles": [RoleDao.get_roles(user.id).name], "menus": menuslist}

    return ResponseUtil.success(res)


@login_check
def list(request):
    pageNum = request.GET.get("pageNum")
    pageSize = request.GET.get("pageSize")
    keyword = request.GET.get("keyword")
    data = UserDao.list_users(pageNum, pageSize, keyword)
    return ResponseUtil.success(data)


@login_check
def roles_all(request):
    data = RoleDao.get_all()
    return ResponseUtil.success(data)
