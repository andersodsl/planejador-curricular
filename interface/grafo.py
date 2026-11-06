import streamlit as st

from services.pre_requisitos import listar_pre_requisitos


def escapar_texto(texto):
    """Prepara textos para serem exibidos nos nós do grafo."""
    return (
        str(texto)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
    )


def render(disciplinas):
    st.header("Visualização do grafo de pré-requisitos")

    st.write(
        "O grafo representa as dependências entre as disciplinas. "
        "As setas indicam que uma disciplina é pré-requisito de outra."
    )

    if not disciplinas:
        st.info("Cadastre disciplinas para visualizar o grafo.")
        return

    # Relaciona o identificador de cada disciplina aos seus dados.
    mapa_disciplinas = {
        str(disciplina["id"]): disciplina
        for disciplina in disciplinas
    }

    # Início da estrutura do grafo.
    linhas = [
        "digraph G {",
        'rankdir="LR";',
        'node [shape="box", style="rounded,filled", '
        'fillcolor="#E8F0FE", color="#4285F4"];',
        'edge [color="#555555", arrowsize="0.8"];'
    ]

    # Adiciona todas as disciplinas como nós.
    for indice, disciplina in enumerate(disciplinas):
        identificador = f"disciplina_{indice}"

        nome = escapar_texto(disciplina["nome"])
        codigo = escapar_texto(disciplina["codigo"])
        periodo = disciplina["periodo"]

        rotulo = escapar_texto(
    f"{codigo}\n{nome}\n{periodo}º período"
)

        linhas.append(
            f'{identificador} [label="{rotulo}"];'
        )

    # Relaciona os identificadores do banco aos nós do grafo.
    identificadores_nos = {
        str(disciplina["id"]): f"disciplina_{indice}"
        for indice, disciplina in enumerate(disciplinas)
    }

    total_relacionamentos = 0

    # Busca os pré-requisitos de cada disciplina.
    for disciplina in disciplinas:
        relacionamentos = listar_pre_requisitos(
            disciplina["codigo"]
        )

        for relacao in relacionamentos:
            origem_id = str(relacao["in"])
            destino_id = str(relacao["out"])

            if (
                origem_id in identificadores_nos
                and destino_id in identificadores_nos
            ):
                origem = identificadores_nos[origem_id]
                destino = identificadores_nos[destino_id]

                linhas.append(
                    f"{origem} -> {destino};"
                )

                total_relacionamentos += 1

    linhas.append("}")

    # Monta o código final do grafo.
    grafo = "\n".join(linhas)

    st.subheader("Grafo de disciplinas")

    st.graphviz_chart(
        grafo,
        use_container_width=True
    )

    st.caption(
        f"Total de disciplinas: {len(disciplinas)} | "
        f"Total de relacionamentos: {total_relacionamentos}"
    )

    st.info(
        "Exemplo: se Lógica de Programação aponta para "
        "Programação Orientada a Objetos, significa que "
        "a primeira é pré-requisito da segunda."
    )