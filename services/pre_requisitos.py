
from database.conexao import conectar
from services.disciplinas import buscar_disciplina


def inicializar_tabela_pre_requisitos():
    with conectar() as db:
        db.query("""
            DEFINE TABLE IF NOT EXISTS prerequisito
            TYPE RELATION
            SCHEMALESS;
        """)


def adicionar_pre_requisito(codigo_origem, codigo_destino):

    inicializar_tabela_pre_requisitos()

    disciplina_origem = buscar_disciplina(codigo_origem)
    disciplina_destino = buscar_disciplina(codigo_destino)

    if disciplina_origem is None:
        raise ValueError("Disciplina de origem não encontrada.")

    if disciplina_destino is None:
        raise ValueError("Disciplina de destino não encontrada.")

    if disciplina_origem["id"] == disciplina_destino["id"]:
        raise ValueError(
            "Uma disciplina não pode ser pré-requisito dela mesma."
        )

    with conectar() as db:

        resultado = db.query(
            """
            SELECT * FROM prerequisito
            WHERE in = $origem AND out = $destino
            """,
            {
                "origem": disciplina_origem["id"],
                "destino": disciplina_destino["id"]
            }
        )

        if resultado:
            raise ValueError(
                "Esse pré-requisito já está cadastrado."
            )

        resultado = db.query(
            """
            RELATE $origem->prerequisito->$destino
            """,
            {
                "origem": disciplina_origem["id"],
                "destino": disciplina_destino["id"]
            }
        )

        return resultado[0] if resultado else None


def listar_pre_requisitos(codigo):

    inicializar_tabela_pre_requisitos()

    disciplina = buscar_disciplina(codigo)

    if disciplina is None:
        raise ValueError("Disciplina não encontrada.")

    with conectar() as db:
        return db.query(
            """
            SELECT * FROM prerequisito
            WHERE out = $disciplina
            """,
            {
                "disciplina": disciplina["id"]
            }
        )

def listar_dependentes(codigo):

    inicializar_tabela_pre_requisitos()

    disciplina = buscar_disciplina(codigo)

    if disciplina is None:
        raise ValueError("Disciplina não encontrada.")

    with conectar() as db:
        return db.query(
            """
            SELECT * FROM prerequisito
            WHERE in = $disciplina
            """,
            {
                "disciplina": disciplina["id"]
            }
        )


def remover_pre_requisito(codigo_origem, codigo_destino):

    inicializar_tabela_pre_requisitos()

    disciplina_origem = buscar_disciplina(codigo_origem)
    disciplina_destino = buscar_disciplina(codigo_destino)

    if disciplina_origem is None:
        raise ValueError("Disciplina de origem não encontrada.")

    if disciplina_destino is None:
        raise ValueError("Disciplina de destino não encontrada.")

    with conectar() as db:

        resultado = db.query(
            """
            SELECT * FROM prerequisito
            WHERE in = $origem AND out = $destino
            """,
            {
                "origem": disciplina_origem["id"],
                "destino": disciplina_destino["id"]
            }
        )

        if not resultado:
            return False

        db.query(
            """
            DELETE prerequisito
            WHERE in = $origem AND out = $destino
            """,
            {
                "origem": disciplina_origem["id"],
                "destino": disciplina_destino["id"]
            }
        )

        return True
