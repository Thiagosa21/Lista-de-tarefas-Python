# Inicia o programa com a lista de tarefas vazia
lista_tarefas = []

# Função que mostra o menu e retorna a opção do usuário
def mostra_menu():
    resposta = input("""
Digite o índice da opção que deseja executar:
----------------------------------
|       Lista de Tarefas         |
----------------------------------
|    1 - Adicionar tarefa        |
|    2 - Ver tarefas             |
|    3 - Concluir tarefa         |
|    4 - Remover tarefa          |
|    5 - Exportar lista em texto |
|    6 - Sair do programa        |
|________________________________|
""")
    return resposta

# Função que adiciona a tarefa na lista
def adiciona_tarefa(resposta):
    lista_tarefas.append(resposta)
    print("Tarefa adicionada com sucesso!")

# Função que mostra a lista ao usuário
def ver_tarefas():
    if not lista_tarefas:
        print("Nenhuma tarefa na lista")
        return
    print("Aqui estão todas as tarefas adicionadas: ")
    for indice, tarefa in enumerate(lista_tarefas):
        print(indice, "-", tarefa)

# Função que marca com "✔" as tarefas que foram concluídas
def concluir_tarefa(indice_concluir):
    lista_tarefas[indice_concluir] += " [✔]"

# Função que retira uma atividade da lista
def remove_tarefa(indice_remover):
    lista_tarefas.pop(indice_remover)


# A opção que for selecionada no menu será executada nas condições abaixo
while True:
    resposta = mostra_menu()

    # De acordo com a opção selecionada, uma função será chamada
    if resposta == "1":
        tarefa = str(input("Digite a tarefa que deseja adicionar: "))
        adiciona_tarefa(tarefa)
    elif resposta == "2":
        print("Aqui estão todas as tarefas da lista:")
        ver_tarefas()

    # Trata o erro caso o usuário digite valores/caracteres não válidos
    elif resposta == "3":
        try:
            indice_concluir = int(input("Digite o índice da tarefa que deseja concluir: "))
            if 0 <= indice_concluir < len(lista_tarefas):
                concluir_tarefa(indice_concluir)
                print("Tarefa cloncluida com sucesso!")
            else:
                print("Índice inválido!")
        except ValueError:
            print("Por favor, digite apenas números!")

    elif resposta == "4":
        try:
            indice_remover = int(input("Digite o índice da tarefa que deseja remover da lista: "))
            if 0 <= indice_remover < len(lista_tarefas):
                remove_tarefa(indice_remover)
                print("Tarefa removida com sucesso!")
            else:
                print("Índice inválido!")
        except ValueError:
            print("Por favor, digite apenas números!")

    elif resposta == "5":
        with open("Lista_de_tarefas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("Aqui estão todas as suas tarefas:\n")
            for tarefa in lista_tarefas:
                arquivo.write(tarefa + "\n")
        print("Lista salva com sucesso em 'Lista_de_tarefas.txt'!")

    elif resposta == "6":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Por favor, digite um valor válido")