from django.contrib import admin
from django.urls import path
from tarefa.views import ListaTarefa, AtualizarTarefa, NovaTarefa, DeletarTarefa, ListaTarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista/', ListaTarefa.as_view(), name='lista'),
    path('nova/', NovaTarefa.as_view(), name='nova'),
    path('tarefa/<int:pk>/update', AtualizarTarefa.as_view(), name='atualizar'),
    path('tarefa/<int:pk>/delete', DeletarTarefa.as_view(), name='deletar'),
]
