import os
import platform
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


#CONFIGURAÇÃO DO BANCO DE DADOS E ORM
engine = create_engine('sqlite:///biblioteca.db', echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


#MODELO DA CLASSE 
class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    emprestado = Column(Boolean, default=False)

    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.emprestado = False

Base.metadata.create_all(engine)

#FUNÇÕES DO SISTEMA
def cadastrar_livro():
    limpar_tela()
    print("=== CADASTRAR LIVRO ===\n")
    nome_livro = input('Digite o nome do livro a ser cadastrado: ')
    autor_livro = input('Digite o nome do autor do livro: ')
    
    novo_livro = Livro(nome_livro, autor_livro)
    
    session.add(novo_livro)
    session.commit()
    print('\nLivro cadastrado com sucesso!!')
    input("\nPressione Enter para voltar ao menu...")

def mostra_livro_cadastrado(pausa=False):
    limpar_tela()
    print("=== LIVROS CADASTRADOS ===\n")
    livros = session.query(Livro).all()
    
    if not livros:
        print("Não existem livros Cadastrados!!")
    else:
        for livro in livros:
            status = "Livro emprestado" if livro.emprestado else "Livro disponível"
            print(f"ID: {livro.id} | Nome: {livro.nome} | Autor: {livro.autor} | Status do livro: {status}")
    
   
    if pausa:
        input("\nPressione Enter para voltar ao menu...")

def empresta_livro():
    livros = session.query(Livro).all()
    if livros:
        mostra_livro_cadastrado(pausa=False)
        print("\n=== EMPRESTAR LIVRO ===")
        id_procurado = int(input("Digite o ID do livro que deseja emprestar: "))
        
        livro = session.query(Livro).filter_by(id=id_procurado).first()
        
        if livro:
            if livro.emprestado:
                print("\nEste livro já está emprestado!")
            else:
                livro.emprestado = True
                session.commit()
                print("\nLivro emprestado com sucesso!")
        else:
            print("\nDigite um ID válido de livro!")
    else:
        limpar_tela()
        print("Você precisa cadastrar um livro primeiro!")
        
    input("\nPressione Enter para voltar ao menu...")

def devolver_livro():
    livros = session.query(Livro).all()
    if livros:
        mostra_livro_cadastrado(pausa=False)
        print("\n=== DEVOLVER LIVRO ===")
        id_procurado = int(input("Digite o ID do livro que deseja devolver: "))
        
        livro = session.query(Livro).filter_by(id=id_procurado).first()
        
        if livro:
            if livro.emprestado:
                livro.emprestado = False
                session.commit()
                print("\nLivro devido com sucesso!")
            else:
                print("\nEste livro não está emprestado!")
        else:
            print("\nDigite um ID válido de livro!")
    else:
        limpar_tela()
        print("Você precisa cadastrar um livro primeiro!")
        
    input("\nPressione Enter para voltar ao menu...")

def remover_livro():
    livros = session.query(Livro).all()
    if livros:
        mostra_livro_cadastrado(pausa=False)
        print("\n=== REMOVER LIVRO ===")
        id_procurado = int(input("Digite o ID do livro que deseja REMOVER da biblioteca: "))
        
        livro = session.query(Livro).filter_by(id=id_procurado).first()
        
        if livro:
            session.delete(livro)
            session.commit()
            print("\nLivro removido do sistema com sucesso!")
        else:
            print("\nDigite um ID válido de livro!")
    else:
        limpar_tela()
        print("Não existem livros cadastrados para remover!")
        
    input("\nPressione Enter para voltar ao menu...")

#MENU PRINCIPAL 
while True:
    limpar_tela() #Garante que o menu limpe as operações anteriores ao voltar
    resposta = int(input("""
    ======================================================
    |                Cadastro de livros                  |
    ======================================================
    |                1 - Cadastrar Livros                |
    |                2 - Mostrar Livros Cadastrados      |
    |                3 - Emprestar Livro                 |
    |                4 - Devolver Livro                  |
    |                5 - Remover Livro                   |
    |                6 - Sair                            |
    ======================================================     
    Qual Opção deseja:         
    """))
    
    if resposta > 6 or resposta < 1:
        print("Digite um número válido!")
        input("\nPressione Enter para tentar novamente...")
    elif resposta == 1:
        cadastrar_livro()
    elif resposta == 2:
        mostra_livro_cadastrado(pausa=True)
    elif resposta == 3:
        empresta_livro()
    elif resposta == 4:
        devolver_livro()
    elif resposta == 5:
        remover_livro()
    elif resposta == 6:
        limpar_tela()
        print("Saindo do sistema...")
        break