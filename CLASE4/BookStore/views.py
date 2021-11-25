from django.http import request
from django.shortcuts import render

# Create your views here.


def bookList(request):
    return render(
        request,
        'BookStore/bookList.html',
        {}
    )


def bookDetail(request):
    return render(
        request,
        'BookStore/bookDetail.html',
        {}
    )


