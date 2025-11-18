from django.contrib import admin
from main.models import Task

#admin.site.register(Task)
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','usuario')
    list_filter = ('concluida', 'prioridade')
    search_fields =('titulo',)