import json
import os

ARQUIVO_JSON = "tarefas.json"

# FUNÇÕES DE PERSISTÊNCIA (JSON)
def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON, se ele existir."""
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []
    return []

def salvar_no_json(lista_tarefas):
    """Salva a lista atual de tarefas no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista_tarefas, arquivo, ensure_ascii=False, indent=4)

# Inicia o programa carregando as tarefas salvas anteriormente
lista_tarefas = carregar_tarefas()

# FUNÇÃO DO MENU
def mostra_menu():
    resposta = input("""
Digite o índice da opção que deseja executar:
----------------------------------
|        Lista de Tarefas        |
----------------------------------
|    1 - Adicionar tarefa        |
|    2 - Ver tarefas             |
|    3 - Concluir tarefa         |
|    4 - Remover tarefa          |
|    5 - Salvar em JSON          |
|    6 - Exportar lista em TXT   |
|    7 - Sair do programa        |
|________________________________|
""")
    return resposta

# FUNÇÕES DE MANIPULAÇÃO
def adiciona_tarefa(tarefa):
    # Salvando como dicionário para controlar melhor se está concluída ou não
    lista_tarefas.append({"texto": tarefa, "concluida": False})
    salvar_no_json(lista_tarefas)
    print("Tarefa adicionada com sucesso!")

def ver_tarefas():
    if not lista_tarefas:
        print("Nenhuma tarefa na lista.")
        return
    print("\nAqui estão todas as tarefas adicionadas:")
    for indice, item in enumerate(lista_tarefas):
        status = "[✔]" if item["concluida"] else "[ ]"
        print(f"{indice} - {item['texto']} {status}")

def concluir_tarefa(indice_concluir):
    if lista_tarefas[indice_concluir]["concluida"]:
        print("Esta tarefa já está concluída!")
    else:
        lista_tarefas[indice_concluir]["concluida"] = True
        salvar_no_json(lista_tarefas)
        print("Tarefa concluída com sucesso!")

def remove_tarefa(indice_remover):
    lista_tarefas.pop(indice_remover)
    salvar_no_json(lista_tarefas)
    print("Tarefa removida com sucesso!")

# LOOP PRINCIPAL
while True:
    resposta = mostra_menu()

    if resposta == "1":
        tarefa = input("Digite a tarefa que deseja adicionar: ").strip()
        if tarefa:
            adiciona_tarefa(tarefa)
        else:
            print("A tarefa não pode estar vazia!")

    elif resposta == "2":
        ver_tarefas()

    elif resposta == "3":
        try:
            indice_concluir = int(input("Digite o índice da tarefa que deseja concluir: "))
            if 0 <= indice_concluir < len(lista_tarefas):
                concluir_tarefa(indice_concluir)
            else:
                print("Índice inválido!")
        except ValueError:
            print("Por favor, digite apenas números!")

    elif resposta == "4":
        try:
            indice_remover = int(input("Digite o índice da tarefa que deseja remover da lista: "))
            if 0 <= indice_remover < len(lista_tarefas):
                remove_tarefa(indice_remover)
            else:
                print("Índice inválido!")
        except ValueError:
            print("Por favor, digite apenas números!")

    elif resposta == "5":
        salvar_no_json(lista_tarefas)
        print(f"Lista salva com sucesso em '{ARQUIVO_JSON}'!")

    elif resposta == "6":
        with open("Lista_de_tarefas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("Aqui estão todas as suas tarefas:\n")
            for item in lista_tarefas:
                status = "[✔]" if item["concluida"] else "[ ]"
                arquivo.write(f"- {item['texto']} {status}\n")
        print("Lista exportada com sucesso em 'Lista_de_tarefas.txt'!")

    elif resposta == "7":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Por favor, digite um valor válido (opções de 1 a 7).")
