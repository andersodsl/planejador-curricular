
from services.disciplinas import listar_disciplinas


print("INICIANDO TESTE DE CONEXAO")

try:
    disciplinas = listar_disciplinas()

    print("\nConexao com o SurrealDB realizada com sucesso!")
    print(f"Quantidade de disciplinas encontradas: {len(disciplinas)}")

except Exception as erro:
    print("\nERRO NA CONEXAO COM O BANCO:")
    print(repr(erro))
    raise SystemExit(1)
