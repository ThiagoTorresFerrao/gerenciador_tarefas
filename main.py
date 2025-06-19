from services.gerenciador import GerenciadorTarefas
from models.tarefa import Tarefa

def menu():
    g = GerenciadorTarefas()
    while True:
        print("\n===== Gerenciador de Tarefas =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (baixa/média/alta): ")
            prazo = input("Prazo (YYYY-MM-DD): ")
            tarefa = Tarefa(titulo, descricao, prioridade, prazo)
            g.adicionar_tarefa(tarefa)
            print("Tarefa adicionada com sucesso!")

        elif opcao == '2':
            g.listar_tarefas()

        elif opcao == '3':
            g.listar_tarefas()
            indice = int(input("Digite o número da tarefa concluída: ")) - 1
            g.concluir_tarefa(indice)
            print("Tarefa marcada como concluída!")

        elif opcao == '4':
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()
