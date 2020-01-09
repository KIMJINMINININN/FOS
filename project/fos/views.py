from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

def index(request):
    if request.method == 'GET':
        return render(request, 'fos/index.html')