import json
import time

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import jwt


def login(request):
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj["username"]
    password = json_obj["password"]
    res = {"tokenHead": "Bearer", "token": make_token("admin")}
    return JsonResponse({"code": 200, "message": "成功", "data": res})


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {"username": username, "exp": now + expire}
    return jwt.encode(payload, key, algorithm="HS256")
