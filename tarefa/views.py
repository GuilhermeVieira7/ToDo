from .models import Tarefa
from django.shortcuts import render
from .forms import TarefaForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Listar tarefas
class ListaTarefa(ListView):
    model = Tarefa
    template_name = 'lista.html'
    context_object_name = 'tarefas'

 # Nova Tarefa 
class NovaTarefa(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'nova.html'
    success_url = '/lista'

# Atulizar Tarefas
class AtualizarTarefa(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'atualizar.html'
    success_url  ='/lista'

# Apagar tarefas atualizadas
class DeletarTarefa(DeleteView):
    model = Tarefa
    template_name = 'deletar.html'
    success_url = '/lista'

def lista_tarefas(request):
    query = request.GET.get('q')
    if query:
        tarefas = Tarefa.objects.filter(nome_tarefa__icontains=query)
    else:
        tarefas = Tarefa.objects.all()
    
    context = {'tarefas': tarefas}
    return render(request, 'lista.html', context)