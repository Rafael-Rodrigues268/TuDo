from django.urls import path
from main.views import TaskList
from . import views 
urlpatterns = [
    path("", TaskList.as_view(), name = 'task_list'),
    path("funcao/", views.task_list,name='task_list_funcao'),
    path("missao_completa/",views.task_completas, name='task_list_completa'),
    path("missao_incompletas/",views.task_imcompletas, name='task_incompletas')
]
