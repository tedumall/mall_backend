from django.urls import path

from users import views

urlpatterns =[
    path("info",views.info),
    path("list",views.list),
    path("role/listAll",views.roles_all)
]