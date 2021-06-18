from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.
def index(request):
    mydictionary = {
        "alltodos" : ToDo.objects.all()
    }
    return render(request, 'index.html' ,context = mydictionary)

def createTask(request):
    return render(request,'createTask.html')

def submit(request):
    obj = ToDo()
    obj.task = request.GET['task'],
    obj.description = request.GET['description'],
    obj.priority = request.GET['inlineRadioOptions'],
    obj.save()
    return render(request,'index.html')