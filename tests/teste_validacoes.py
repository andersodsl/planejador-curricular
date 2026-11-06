
from services.disciplinas import cadastrar_disciplina


def executar_teste(titulo, dados):
    print(f"\n{titulo}")

    try:
        cadastrar_disciplina(**dados)
        print("ERRO: o cadastro deveria ter sido rejeitado.")

    except ValueError as erro:
        print("Validação aprovada:", erro)

    except Exception as erro:
        print("Erro inesperado:", repr(erro))


# Teste 1: nome vazio
executar_teste(
    "TESTE 1 - Nome vazio",
    {
        "nome": "",
        "codigo": "TEST101",
        "periodo": 1,
        "carga_horaria": 60,
        "descricao": "Teste"
    }
)

# Teste 2: código vazio
executar_teste(
    "TESTE 2 - Código vazio",
    {
        "nome": "Disciplina Teste",
        "codigo": "   ",
        "periodo": 1,
        "carga_horaria": 60,
        "descricao": "Teste"
    }
)

# Teste 3: período inválido
executar_teste(
    "TESTE 3 - Período zero",
    {
        "nome": "Disciplina Teste",
        "codigo": "TEST102",
        "periodo": 0,
        "carga_horaria": 60,
        "descricao": "Teste"
    }
)

# Teste 4: carga horária negativa
executar_teste(
    "TESTE 4 - Carga horária negativa",
    {
        "nome": "Disciplina Teste",
        "codigo": "TEST103",
        "periodo": 1,
        "carga_horaria": -20,
        "descricao": "Teste"
    }
)

# Teste 5: código duplicado
executar_teste(
    "TESTE 5 - Código já cadastrado",
    {
        "nome": "Outra Lógica de Programação",
        "codigo": "ADS001",
        "periodo": 1,
        "carga_horaria": 60,
        "descricao": "Teste de duplicidade"
    }
)
