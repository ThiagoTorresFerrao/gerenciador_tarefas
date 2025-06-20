import os
import json
from models.tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self, arquivo='data/tarefas.json'):
        self.arquivo = arquivo
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
                return [Tarefa(**t) for t in dados]
        return []

    def salvar_tarefas(self):
        with open(self.arquivo, 'w') as f:
            json.dump([t.to_dict() for t in self.tarefas], f, indent=4)

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        self.salvar_tarefas()

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, 1):
            status = "✔" if tarefa.concluida else "✘"
            print(f"{i}. [{status}] {tarefa.titulo} - Prioridade: {tarefa.prioridade}, Prazo: {tarefa.prazo}")

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            self.salvar_tarefas()

    def contar_tarefas(self):
        """Retorna o total de tarefas cadastradas."""
        return len(self.tarefas)
