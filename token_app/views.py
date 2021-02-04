import json

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def login(request):

    print(request)
    json_str = request.body
    # json_obj = json.loads(json_str)
    print(json_str)
    return JsonResponse()
