
import uuid

from services.disciplinas import (
    cadastrar_disciplina,
    buscar_disciplina,
    excluir_disciplina
)

from services.pre_requisitos import (
    adicionar_pre_requisito,
    listar_pre_requisitos,
    listar_dependentes,
    remover_pre_requisito
)


print("INICIANDO TESTES DE PRE-REQUISITOS")

identificador = uuid.uuid4().hex[:8].upper()

codigo_origem = f"TESTE{identificador}A"
codigo_destino = f"TESTE{identificador}B"

origem_criada = False
destino_criada = False

try:
   
    cadastrar_disciplina(
        nome="Disciplina Origem Teste",
        codigo=codigo_origem,
        periodo=1,
        carga_horaria=60,
        descricao="Disciplina temporaria para teste de grafo."
    )
    origem_criada = True

    cadastrar_disciplina(
        nome="Disciplina Destino Teste",
        codigo=codigo_destino,
        periodo=2,
        carga_horaria=60,
        descricao="Disciplina temporaria para teste de grafo."
    )
    destino_criada = True

    disciplina_origem = buscar_disciplina(codigo_origem)
    disciplina_destino = buscar_disciplina(codigo_destino)

    print("\nTESTE 1 - Adicionar pre-requisito")

    resultado = adicionar_pre_requisito(
        codigo_origem,
        codigo_destino
    )

    assert resultado, "O relacionamento nao foi criado."
    print("Aprovado: relacionamento criado.")

    print("\nTESTE 2 - Listar pre-requisitos")

    resultado = listar_pre_requisitos(codigo_destino)

    assert any(
        str(relacao["in"]) == str(disciplina_origem["id"])
        for relacao in resultado
    ), "O pre-requisito nao foi encontrado."

    print("Aprovado: pre-requisito encontrado.")

    print("\nTESTE 3 - Listar disciplinas dependentes")

    resultado = listar_dependentes(codigo_origem)

    assert any(
        str(relacao["out"]) == str(disciplina_destino["id"])
        for relacao in resultado
    ), "A disciplina dependente nao foi encontrada."

    print("Aprovado: disciplina dependente encontrada.")

    print("\nTESTE 4 - Impedir relacionamento duplicado")

    try:
        adicionar_pre_requisito(
            codigo_origem,
            codigo_destino
        )

        raise AssertionError(
            "O sistema permitiu um relacionamento duplicado."
        )

    except ValueError as erro:
        print("Aprovado:", erro)

    print("\nTESTE 5 - Remover relacionamento")

    resultado = remover_pre_requisito(
        codigo_origem,
        codigo_destino
    )

    assert resultado, "O relacionamento nao foi removido."
    print("Aprovado: relacionamento removido.")

    print("\nTESTE 6 - Confirmar remocao")

    resultado = listar_pre_requisitos(codigo_destino)

    assert not any(
        str(relacao["in"]) == str(disciplina_origem["id"])
        for relacao in resultado
    ), "O relacionamento ainda existe."

    print("Aprovado: relacionamento nao existe mais.")

    print("\nTODOS OS TESTES FORAM APROVADOS!")

except Exception as erro:
    print("\nERRO DURANTE OS TESTES:")
    print(repr(erro))
    raise

finally:

    try:
        remover_pre_requisito(
            codigo_origem,
            codigo_destino
        )
    except Exception:
        pass

    if destino_criada:
        excluir_disciplina(codigo_destino)

    if origem_criada:
        excluir_disciplina(codigo_origem)

    print("\nLimpeza dos dados temporarios concluida.")
