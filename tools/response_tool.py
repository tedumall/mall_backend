from django.http import JsonResponse
from enum import Enum


class ResponseUtil:
    @staticmethod
    def build_response(code, message, data=None):
        return JsonResponse({"code": code, "message": message, "data": data})

    @staticmethod
    def success(data):
        result = ResultCode.SUCCESS.value
        code = result[0]
        msg = result[1]
        return ResponseUtil.build_response(code, msg, data)

    @staticmethod
    def failed():
        result = ResultCode.FAILED.value
        code = result[0]
        msg = result[1]
        return ResponseUtil.build_response(code, msg)

    @staticmethod
    def validateFailed(msg):
        """
     参数验证失败返回结果
        :param msg 提示信息:
        :return:
        """
        result = ResultCode.VALIDATE_FAILED.value
        code = result[0]
        return ResponseUtil.build_response(code, msg)

    @staticmethod
    def unauthorized():
        result = ResultCode.UNAUTHORIZED.value
        code = result[0]
        msg = result[1]
        return ResponseUtil.build_response(code, msg)

    @staticmethod
    def forbidden():
        result = ResultCode.FORBIDDEN.value
        code = result[0]
        msg = result[1]
        return ResponseUtil.build_response(code, msg)


class ResultCode(Enum):
    """
     枚举了一些常用API操作码
    """
    SUCCESS = (200, "操作成功")
    FAILED = (500, "操作失败")
    VALIDATE_FAILED = (404, "参数检验失败")
    UNAUTHORIZED = (401, "暂未登录或token已经过期")
    FORBIDDEN = (403, "没有相关权限")
