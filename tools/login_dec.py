import jwt
from django.conf import settings

from tools.response_tool import ResponseUtil
from users.models import UmsAdmin


def login_check(func):
    """
    登录用户检查
    :param func:
    :return:
    """

    def wrap(request, *args, **kwargs):
        # 从request中拿到token
        token = request.META.get("HTTP_AUTHORIZATION")[6:]
        if not token:
            return ResponseUtil.unauthorized()
        try:
            payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms="HS256")
        except:
            return ResponseUtil.unauthorized()

        username = payload["username"]
        user = UmsAdmin.objects.get(username=username)
        request.myuser = user
        # 调用装饰的函数
        return func(request, *args, **kwargs)

    return wrap


def get_user_by_request(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    if not token:
        # 未登录
        return None
    try:
        payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms="HS256")
    except:
        # token失效
        return None
    username = payload["username"]
    return username
