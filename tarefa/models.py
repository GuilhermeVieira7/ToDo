from django.db import models

# Create your models here.

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    nome_tarefa = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.nome_tarefa