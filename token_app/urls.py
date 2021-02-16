from django.urls import path

from token_app import views

urlpatterns =[
    path("login",views.login),
    path("logout",views.logout)
]