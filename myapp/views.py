from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def toDoList(request):
    mydictionary = {
        "alltodos" : ToDo.objects.all()
    }
    return render(request,'todoList.html', context = mydictionary)

# def submit(request):
#     if request.is_ajax():
#         obj = ToDo()
#         task = request.GET['task'],
#         obj.task = task,
#         description = request.GET['description'],
#         obj.description = description,
#         priority = request.GET['inlineRadioOptions'],
#         obj.priority = priority,
#         obj.save()
#         if obj.task and obj.description :
#             return JsonResponse("Your task has been added successfully", safe = False)
#         else:
#             return JsonResponse("It FAILED",safe= False)
#     else:
#         return JsonResponse("not ajax", safe=False )

# def submit(request):
#     obj = ToDo()
#     print("im calling TO DO"),
#     task = request.POST.get('task'),
#     obj.task = task,
#     description = request.POST.get('description'),
#     obj.description = description,
#     priority = request.POST.get('inlineRadioOptions'),
#     obj.priority = priority,
#     print("i gotten task, descirption , and priority "),
#     obj.save()
#     if obj.task and obj.description :
#         return JsonResponse("Your task has been added successfully", safe = False)
#     else:
#         return JsonResponse("It FAILED",safe= False)

# def submit(request):
#     form = TaskForm(request.POST or None)
#     data = {}
#     # if request.method == 'POST':
#     #     form = TaskForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('createTask')
#     if request.is_ajax():
#         if form.is_valid():
#             form.save()
#             data['task'] = form.cleaned_data.get('task')
#             data['status'] = 'ok'
#             return JsonResponse(data)
        
#     context = {
#         'form' : form,
#     }

    return render(request, 'createTask.html', context)
def submit(request):
    if request.method == "POST" and request.is_ajax:
        form = TaskForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return JsonResponse({"msg" : "ToDo Saved", "task" : task})
        else:
            return JsonResponse({"msg": "InvalidTask","task":"none"})
    else:
        form = TaskForm()
        return render(request, 'index.html',{"form":"form"})