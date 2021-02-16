from django.core.paginator import Paginator
from django.db.models import Q

from users.models import UmsAdmin


class UserDao:
    @staticmethod
    def list_users(pageNum, pageSize, keyword=None):
        """
        分页查询
        :param pageNum:第几页
        :param pageSize:每页几个数据
        :param keyword:关键字
        :return:
        """
        user_list = UmsAdmin.objects.all()
        if keyword:
            user_list = user_list.filter(Q(username__contains=keyword) | Q(nick_name__contains=keyword))

        res_list = []
        for user in user_list:
            res_list.append(user.serize())

        # 分页查询
        paginator = Paginator(res_list, pageSize)
        page = paginator.page(pageNum)
        # print(page.object_list)
        data = {}
        data["pageNum"] = pageNum
        data["pageSize"] = pageSize
        data["totalPage"] = paginator.num_pages
        data["total"] = paginator.count
        data["list"] = page.object_list
        return data
