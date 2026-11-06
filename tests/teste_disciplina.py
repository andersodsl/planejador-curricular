
import uuid

from services.disciplinas import (
    cadastrar_disciplina,
    buscar_disciplina,
    excluir_disciplina
)

from services.pre_requisitos import (
    adicionar_pre_requisito,
    remover_pre_requisito
)


print("TESTES DE EXCLUSAO DE DISCIPLINAS")

identificador = uuid.uuid4().hex[:8].upper()

codigo_origem = f"EXC{identificador}A"
codigo_destino = f"EXC{identificador}B"
codigo_independente = f"EXC{identificador}C"

codigos_criados = []
relacionamento_criado = False

try:
    # Criar tres disciplinas temporarias.
    for codigo, nome in [
        (codigo_origem, "Disciplina Origem Teste"),
        (codigo_destino, "Disciplina Destino Teste"),
        (codigo_independente, "Disciplina Independente Teste")
    ]:
        cadastrar_disciplina(
            nome=nome,
            codigo=codigo,
            periodo=1,
            carga_horaria=60,
            descricao="Registro temporario para teste."
        )
        codigos_criados.append(codigo)

    print("\nTESTE 1 - Excluir disciplina sem relacionamento")

    resultado = excluir_disciplina(codigo_independente)

    assert resultado is True
    assert buscar_disciplina(codigo_independente) is None

    print("Aprovado: disciplina independente excluida.")

    print("\nCriando relacionamento entre disciplinas...")

    adicionar_pre_requisito(codigo_origem, codigo_destino)
    relacionamento_criado = True

    print("Relacionamento criado.")

    print("\nTESTE 2 - Impedir exclusao da disciplina de origem")

    try:
        excluir_disciplina(codigo_origem)
        raise AssertionError(
            "O sistema permitiu excluir uma disciplina relacionada."
        )

    except ValueError as erro:
        print("Aprovado:", erro)

    print("\nTESTE 3 - Impedir exclusao da disciplina de destino")

    try:
        excluir_disciplina(codigo_destino)
        raise AssertionError(
            "O sistema permitiu excluir uma disciplina relacionada."
        )

    except ValueError as erro:
        print("Aprovado:", erro)

    print("\nTESTE 4 - Confirmar que as disciplinas continuam cadastradas")

    assert buscar_disciplina(codigo_origem) is not None
    assert buscar_disciplina(codigo_destino) is not None

    print("Aprovado: ambas as disciplinas continuam no banco.")

    print("\nTESTE 5 - Remover relacionamento")

    resultado = remover_pre_requisito(
        codigo_origem,
        codigo_destino
    )

    assert resultado is True
    relacionamento_criado = False

    print("Aprovado: relacionamento removido.")

    print("\nTESTE 6 - Excluir disciplinas após remover relacionamento")

    assert excluir_disciplina(codigo_origem) is True
    assert excluir_disciplina(codigo_destino) is True

    print("Aprovado: disciplinas excluidas após remover o relacionamento.")

    print("\nTODOS OS TESTES FORAM APROVADOS!")

except Exception as erro:
    print("\nERRO DURANTE OS TESTES:")
    print(repr(erro))
    raise

finally:
    # Garantir a limpeza dos registros temporarios.
    if relacionamento_criado:
        try:
            remover_pre_requisito(codigo_origem, codigo_destino)
        except Exception:
            pass

    for codigo in codigos_criados:
        try:
            excluir_disciplina(codigo)
        except Exception:
            pass

    print("\nLimpeza dos dados temporarios concluida.")
