from django.shortcuts import render

from django.views.generic import TemplateView,  ListView
from main.models import Task


class HomeView(TemplateView):
    template_name = 'home.html'
    
class TaskList(ListView):
    model = Task
    template_name= 'task/task_list.html'
    context_object_name = 'tarefas'

    
 
def task_list(request):
    tarefas = Task.objects.all()
    context = {
        "tarefas":tarefas,
        "Titulo_pagina": 'Quest_RPG_RealLife'
        
    }
    return render (request, 'Task/task_list.html', context)



 
def task_completas(request):
    tarefas = Task.objects.filter(concluida=1)
    context = {
        "tarefas":tarefas,
        "Titulo_pagina": 'Quest_RPG_RealLife_concluidas'
        
    }
    return render (request, 'Task/task_list.html', context)

 
def task_imcompletas(request):
    tarefas = Task.objects.filter(concluida=0)
    context = {
        "tarefas":tarefas,
        "Titulo_pagina": 'Quest_RPG_RealLife_imcompletas'
        
    }
    return render (request, 'Task/task_list.html', context)

