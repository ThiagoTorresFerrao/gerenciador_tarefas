from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, prioridade, prazo, concluida=False, criada_em=None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = concluida
        self.criada_em = criada_em or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def concluir(self):
        self.concluida = True

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'descricao': self.descricao,
            'prioridade': self.prioridade,
            'prazo': self.prazo,
            'concluida': self.concluida,
            'criada_em': self.criada_em
        }
