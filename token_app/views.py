import hashlib
import json
import time

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import jwt

from tools.response_tool import ResponseUtil
from users.models import UmsAdmin


def login(request):
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj["username"]
    password = json_obj["password"]
    try:
        user = UmsAdmin.objects.get(username=username)
    except Exception as e:
        return ResponseUtil.validateFailed("用户名或密码错误")

    md5 = hashlib.md5()
    md5.update(password.encode())
    pass_h = md5.hexdigest()
    if pass_h != user.password:
        return ResponseUtil.validateFailed("用户名或密码错误")

    res = {"tokenHead": "Bearer", "token": make_token("admin")}
    return ResponseUtil.success(res)


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {"username": username, "exp": now + expire}
    return jwt.encode(payload, key, algorithm="HS256")
