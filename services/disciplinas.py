
from database.conexao import conectar

def validar_disciplina(
    nome,
    codigo,
    periodo,
    carga_horaria,
    descricao
):
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("O nome da disciplina é obrigatório.")

    if not isinstance(codigo, str) or not codigo.strip():
        raise ValueError("O código da disciplina é obrigatório.")

    if (
        not isinstance(periodo, int)
        or isinstance(periodo, bool)
        or periodo <= 0
    ):
        raise ValueError("O período deve ser um número inteiro positivo.")

    if (
        not isinstance(carga_horaria, int)
        or isinstance(carga_horaria, bool)
        or carga_horaria <= 0
    ):
        raise ValueError(
            "A carga horária deve ser um número inteiro positivo."
        )

    if descricao is not None and not isinstance(descricao, str):
        raise ValueError("A descrição deve ser um texto.")

    return True

def cadastrar_disciplina(
    nome,
    codigo,
    periodo,
    carga_horaria,
    descricao
):
    validar_disciplina(
        nome,
        codigo,
        periodo,
        carga_horaria,
        descricao
    )

    codigo = codigo.strip()

    disciplina_existente = buscar_disciplina(codigo)

    if disciplina_existente is not None:
        raise ValueError(
            f"Já existe uma disciplina cadastrada com o código {codigo}."
        )

    with conectar() as db:
        resultado = db.create("disciplina", {
            "nome": nome.strip(),
            "codigo": codigo,
            "periodo": periodo,
            "carga_horaria": carga_horaria,
            "descricao": descricao.strip() if descricao else ""
        })

        return resultado


def listar_disciplinas():
    with conectar() as db:
        resultado = db.select("disciplina")

        resultado = sorted(
            resultado,
            key=lambda disciplina: (
                disciplina.get("periodo", 0),
                disciplina.get("codigo", "")
            )
        )

        return resultado

def buscar_disciplina(codigo):
    if not isinstance(codigo, str) or not codigo.strip():
        raise ValueError("Informe um código válido.")

    with conectar() as db:
        resultado = db.query(
            "SELECT * FROM disciplina WHERE codigo = $codigo",
            {
                "codigo": codigo.strip()
            }
        )

        if resultado:
            return resultado[0]

        return None

def atualizar_disciplina(
    codigo,
    nome=None,
    periodo=None,
    carga_horaria=None,
    descricao=None
):
    if not isinstance(codigo, str) or not codigo.strip():
        raise ValueError("Informe um código válido.")

    dados = {}

    if nome is not None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome não pode ficar vazio.")

        dados["nome"] = nome.strip()

    if periodo is not None:
        if (
            not isinstance(periodo, int)
            or isinstance(periodo, bool)
            or periodo <= 0
        ):
            raise ValueError("O período deve ser um inteiro positivo.")

        dados["periodo"] = periodo

    if carga_horaria is not None:
        if (
            not isinstance(carga_horaria, int)
            or isinstance(carga_horaria, bool)
            or carga_horaria <= 0
        ):
            raise ValueError(
                "A carga horária deve ser um inteiro positivo."
            )

        dados["carga_horaria"] = carga_horaria

    if descricao is not None:
        if not isinstance(descricao, str):
            raise ValueError("A descrição deve ser um texto.")

        dados["descricao"] = descricao.strip()

    if not dados:
        raise ValueError("Nenhum dado foi informado para atualização.")

    disciplina = buscar_disciplina(codigo)

    if disciplina is None:
        return None

    with conectar() as db:
        resultado = db.merge(
            disciplina["id"],
            dados
        )

        return resultado

def excluir_disciplina(codigo):
    if not isinstance(codigo, str) or not codigo.strip():
        raise ValueError("Informe um código válido.")

    disciplina = buscar_disciplina(codigo)

    if disciplina is None:
        return False

    with conectar() as db:

        relacionamentos = db.query(
            """
            SELECT * FROM prerequisito
            WHERE in = $disciplina OR out = $disciplina
            """,
            {
                "disciplina": disciplina["id"]
            }
        )

        if relacionamentos:
            raise ValueError(
                "Não é possível excluir esta disciplina porque ela "
                "possui relacionamentos de pré-requisitos. "
                "Remova os relacionamentos antes de excluí-la."
            )

        db.delete(disciplina["id"])

        return True

