lista_tarefas = []

def adicionar_tarefa():
    titulo = input(f'Digite o título da tarefa: ')
    descricao = input(f'Digite a descrição da tarefa: ')
    horario = int(input(f'Digite o horário a fazer: '))
    
    nova_tarefa = {
        "titulo" : titulo,
        "descricao" : descricao,
        "horario" : horario
    }
    lista_tarefas.append(nova_tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

def listar_tarefas():
    if not lista_tarefas:
        print(f'A lista está vazia!')
        return
        
    for i, tarefa in enumerate(lista_tarefas):
        print(f"Tarefa {i + 1}:")
        print(f"  Título: {tarefa['titulo']}")
        print(f"  Descrição: {tarefa['descricao']}")
        print(f"  Horário: {tarefa['horario']}")

def concluir_tarefa():
    titulo = input(f'Digite o título da tarefa que foi concluída: ')
    for tarefa in lista_tarefas:
        if tarefa["titulo"].lower() == titulo.lower():
            print(f"Tarefa '{titulo}' marcada como concluída!")
            return
    print(f'O título {titulo} não está na lista de tarefas.')

def remover_tarefa():
    titulo = input(f'Digite o título da tarefa que deseja remover: ')
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa["titulo"].lower() == titulo.lower():
            lista_tarefas.pop(i)
            print(f"Tarefa '{titulo}' excluída com sucesso!")
            return
    print(f'O título {titulo} não está na lista de tarefas.')

MENSAGEM_INICIO = """
Lista de Tarefas

[1] Adicionar Tarefa
[2] Listar Tarefas
[3] Concluir Tarefa
[4] Remover Tarefa
[0] Sair
"""

def main():
    while True:
        print(MENSAGEM_INICIO)
        choice = int(input(">> "))
        if choice == 1:
            adicionar_tarefa()
        elif choice == 2:
            listar_tarefas()
        elif choice == 3:
            concluir_tarefa()
        elif choice == 4:
            remover_tarefa()
        elif choice == 0:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
