
# 📚 Planejador de Grade Curricular

Sistema desenvolvido como projeto acadêmico para a disciplina de Banco de Dados NoSQL, com o objetivo de gerenciar disciplinas acadêmicas e seus respectivos pré-requisitos.

A aplicação permite cadastrar, consultar, editar e excluir disciplinas, além de estabelecer relacionamentos entre elas e visualizar essas dependências por meio de um grafo.

## 👥 Integrantes

- Anderson Leandro
- Naira Miriam

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| SurrealDB 4.0.0 | Banco de dados NoSQL |
| Streamlit | Desenvolvimento da interface |
| Docker | Execução e persistência do banco |
| Visual Studio Code | Ambiente de desenvolvimento |

## 🗄️ Modelagem do banco de dados

O projeto utiliza dois conceitos de modelagem do SurrealDB: documentos e grafos.

### 1. Documentos — Disciplina

As disciplinas são armazenadas na tabela `disciplina`, contendo os seguintes atributos:

- `nome`: nome da disciplina.
- `codigo`: código identificador.
- `periodo`: período em que a disciplina é ofertada.
- `carga_horaria`: carga horária da disciplina.
- `descricao`: descrição da disciplina.

### 2. Grafos — Pré-requisitos

Os relacionamentos são armazenados na tabela `prerequisito`, definida como uma tabela de relação (`RELATION`).

Cada relacionamento conecta duas disciplinas:

- `in`: disciplina que representa o pré-requisito.
- `out`: disciplina que depende do pré-requisito.

Por exemplo, se Lógica de Programação é pré-requisito de Programação Orientada a Objetos, o grafo representa essa dependência por meio de uma aresta direcionada.

## ⚙️ Funcionalidades

### Visão geral
- Quantidade de disciplinas cadastradas.
- Quantidade de períodos identificados.
- Soma da carga horária.
- Listagem das disciplinas.

### Gerenciamento de disciplinas
- Cadastro de disciplinas.
- Consulta de informações.
- Edição de dados.
- Exclusão de disciplinas.
- Validação de campos obrigatórios e códigos duplicados.
- Proteção contra exclusão de disciplinas que possuem relacionamentos de pré-requisitos.

### Gerenciamento de pré-requisitos
- Adição de relacionamentos.
- Consulta de dependências.
- Remoção de relacionamentos.
- Validação de disciplinas existentes e relacionamentos duplicados.
- Impedimento de relacionamentos de uma disciplina com ela mesma.

### Visualização do grafo
- Representação visual das disciplinas.
- Exibição das conexões entre os pré-requisitos.
- Setas indicando o sentido das dependências.

## 📁 Estrutura do projeto

```text
planejador_curricular/
│
├── backups/
│   └── backup_inicial.surql
│
├── database/
│   └── conexao.py
│
├── interface/
│   ├── __init__.py
│   ├── visao_geral.py
│   ├── disciplinas.py
│   ├── pre_requisitos.py
│   └── grafo.py
│
├── services/
│   ├── disciplinas.py
│   └── pre_requisitos.py
│
├── tests/
│   ├── __init__.py
│   ├── teste_conexao.py
│   ├── teste_disciplina.py
│   ├── teste_pre_requisitos.py
│   └── teste_validacoes.py
│
├── app.py
├── fazer_backup.ps1
├── requirements.txt
├── .gitignore
└── README.md
```

## 💻 Instalação e execução

### 1. Pré-requisitos

- Python instalado.
- Docker Desktop instalado e em execução.
- SurrealDB executado por meio do Docker.

### 2. Criar o ambiente virtual

```powershell
py -m venv .venv
```

Ativar o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 4. Executar o SurrealDB

O banco é executado em um container Docker, utilizando a porta 8001 da máquina local e um volume persistente.

Para criar o container:

```powershell
docker run -d `
  --name surrealdb `
  --restart unless-stopped `
  -p 127.0.0.1:8001:8000 `
  -v surrealdb-data:/data `
  surrealdb/surrealdb:latest `
  start --user root --pass root surrealkv:/data/planejador.db
```

Caso o container já exista, basta iniciá-lo:

```powershell
docker start surrealdb
```

### 5. Executar a aplicação

Na pasta do projeto, com o ambiente virtual ativado:

```powershell
streamlit run app.py
```

A aplicação será disponibilizada pelo Streamlit no endereço local informado no terminal, normalmente:

`http://localhost:8501`

## 💾 Backup e restauração

O projeto possui um script PowerShell para facilitar a exportação do banco de dados.

Para executar:

```powershell
.\fazer_backup.ps1
```

Os arquivos gerados são armazenados na pasta `backups`, com data e horário no nome.

A restauração pode ser realizada por meio do comando de importação do SurrealDB:

```powershell
& "$env:LOCALAPPDATA\SurrealDB\surreal.exe" db import `
  --endpoint http://127.0.0.1:8001 `
  --username root `
  --password root `
  --namespace planejador_curricular `
  --database backup_teste `
  .\backups\backup_inicial.surql
```

A restauração foi testada em um banco separado, permitindo verificar a recuperação dos documentos e dos relacionamentos.

**Observação:** o script realiza a exportação quando executado manualmente. Não há agendamento automático de execução.

## 🧪 Testes realizados

O projeto possui scripts independentes para verificar a conexão, as validações e as operações de disciplinas e pré-requisitos.

Os testes são executados pelo terminal, a partir da pasta principal do projeto, com o ambiente virtual ativado:

| Comando | Objetivo |
|---|---|
| `py -m tests.teste_conexao` | Verificar a conexão com o SurrealDB |
| `py -m tests.teste_validacoes` | Testar as validações dos dados |
| `py -m tests.teste_pre_requisitos` | Testar a criação, consulta e remoção de relacionamentos |
| `py -m tests.teste_disciplina` | Testar a exclusão de disciplinas e a proteção da integridade dos relacionamentos |

Os testes verificam operações de cadastro, consulta, atualização, exclusão, validações, prevenção de duplicidades e gerenciamento dos relacionamentos.

Os testes que criam registros temporários realizam a limpeza desses dados ao final da execução.

## 📌 Considerações sobre o SurrealDB

O SurrealDB permite trabalhar com diferentes modelos de dados em um mesmo sistema, incluindo documentos e grafos.

**Vantagens observadas:**
- Suporte a documentos e relacionamentos em grafo.
- Linguagem de consulta SurrealQL.
- Possibilidade de representar relações direcionadas entre registros.
- Integração com aplicações Python.

**Pontos de atenção:**
- É necessário conhecer a linguagem SurrealQL.
- A configuração e a administração do banco exigem familiaridade com a ferramenta.
- O projeto precisa de cuidados com a integridade dos relacionamentos durante operações de exclusão e atualização.

## 🎓 Objetivo acadêmico

Este projeto foi desenvolvido para aplicar conceitos de bancos de dados NoSQL, explorando o armazenamento documental e a modelagem de grafos em uma aplicação prática de gerenciamento curricular.
