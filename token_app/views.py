import datetime
import hashlib
import json
# Create your views here.
import jwt

from tools.common_tools import make_token
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
    # 更新登录时间
    user.login_time = datetime.datetime.now()
    user.save()
    return ResponseUtil.success(res)


def logout(request):
    return ResponseUtil.success(data=None)
