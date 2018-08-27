from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    # reqeust: HttpRequest
    # numbers = 123/54324/234/234/324
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)



def hello(reqeust, name, age):
    return HttpResponse("안녕하세요. {}. {}살이시네요.".format(name, age))