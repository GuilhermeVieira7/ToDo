from django.contrib import admin
from .models import Tarefa

# Register your models here.

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome_tarefa',)
    search_fields = ('nome_tarefa',)

admin.site.register(Tarefa, TarefaAdmin)