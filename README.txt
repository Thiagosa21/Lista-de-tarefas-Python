# 📝 Gerenciador de Tarefas em Python (CLI)

> Um sistema de lista de tarefas (To-Do List) desenvolvido em Python via linha de comando (CLI), com suporte a persistência de dados em JSON e exportação para arquivos de texto.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.12.8**
* Módulo nativo **`json`** (para persistência e armazenamento de dados)
* Módulo nativo **`os`** (para verificação de arquivos locais)

---

## ⚙️ Funcionalidades

O sistema implementa um fluxo completo de gerenciamento de tarefas:
1. **Adicionar Tarefa:** Insere uma nova atividade na lista.
2. **Ver Tarefas:** Exibe todas as tarefas cadastradas com seus respectivos índices e status (pendente `[ ]` ou concluída `[✔]`).
3. **Concluir Tarefa:** Altera o status de uma tarefa específica para concluída, evitando duplicações.
4. **Remover Tarefa:** Exclui permanentemente uma atividade com base no índice informado.
5. **Salvar em JSON:** Força o salvamento manual do estado atual das tarefas no arquivo local.
6. **Exportar em TXT:** Gera um relatório limpo e formatado em arquivo de texto (`Lista_de_tarefas.txt`).
7. **Sair:** Encerra a aplicação de forma segura.

---

## 🛠️ Como Executar o Projeto Localmente

### Pré-requisitos
* Ter o **Python** instalado na sua máquina.

### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU_USUARIO/nome-do-repositorio.git](https://github.com/SEU_USUARIO/nome-do-repositorio.git)
cd nome-do-repositorio
