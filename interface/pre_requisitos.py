
import streamlit as st

from services.pre_requisitos import (
    adicionar_pre_requisito,
    listar_pre_requisitos,
    remover_pre_requisito
)


def render(disciplinas):

    if "mensagem_sucesso_pre" in st.session_state:
        st.success(st.session_state["mensagem_sucesso_pre"])
        del st.session_state["mensagem_sucesso_pre"]

    st.header("Gerenciamento de pré-requisitos")

    aba_adicionar, aba_consultar, aba_remover = st.tabs(
        ["Adicionar", "Consultar", "Remover"]
    )

    mapa_disciplinas = {
        str(disciplina["id"]): disciplina
        for disciplina in disciplinas
    }

    codigos = [
        disciplina["codigo"]
        for disciplina in disciplinas
    ]

    with aba_adicionar:
        st.subheader("Adicionar relacionamento")

        if len(disciplinas) >= 2:
            codigo_origem = st.selectbox(
                "Disciplina que será o pré-requisito:",
                codigos,
                key="origem"
            )

            codigo_destino = st.selectbox(
                "Disciplina que depende dela:",
                [
                    codigo
                    for codigo in codigos
                    if codigo != codigo_origem
                ],
                key="destino"
            )

            if st.button("Adicionar pré-requisito"):
                try:
                    adicionar_pre_requisito(
                        codigo_origem,
                        codigo_destino
                    )

                    st.session_state["mensagem_sucesso_pre"] = (
                        "Pré-requisito adicionado com sucesso!"
                    )
                    st.rerun()

                except Exception as erro:
                    st.error(str(erro))
        else:
            st.info(
                "É necessário cadastrar pelo menos duas disciplinas."
            )

    with aba_consultar:
        st.subheader("Consultar relacionamentos")

        if disciplinas:
            codigo_consulta = st.selectbox(
                "Selecione uma disciplina:",
                codigos,
                key="consulta_pre"
            )

            try:
                relacionamentos = listar_pre_requisitos(
                    codigo_consulta
                )

                if relacionamentos:
                    for relacao in relacionamentos:
                        origem = mapa_disciplinas.get(
                            str(relacao["in"])
                        )

                        destino = mapa_disciplinas.get(
                            str(relacao["out"])
                        )

                        if origem and destino:
                            st.write(
                                f"**{origem['nome']}** "
                                f"→ pré-requisito de → "
                                f"**{destino['nome']}**"
                            )
                else:
                    st.info(
                        "Esta disciplina não possui pré-requisitos cadastrados."
                    )

            except Exception as erro:
                st.error(str(erro))
        else:
            st.info("Não existem disciplinas cadastradas.")

    with aba_remover:
        st.subheader("Remover relacionamento")

        opcoes = {}

        for disciplina in disciplinas:
            try:
                relacionamentos = listar_pre_requisitos(
                    disciplina["codigo"]
                )

                for relacao in relacionamentos:
                    origem = mapa_disciplinas.get(
                        str(relacao["in"])
                    )

                    destino = mapa_disciplinas.get(
                        str(relacao["out"])
                    )

                    if origem and destino:
                        descricao = (
                            f"{origem['codigo']} - {origem['nome']} "
                            f"→ {destino['codigo']} - {destino['nome']}"
                        )

                        opcoes[descricao] = (
                            origem["codigo"],
                            destino["codigo"]
                        )

            except Exception as erro:
                st.error(str(erro))

        if opcoes:
            selecao = st.selectbox(
                "Selecione o relacionamento:",
                list(opcoes.keys())
            )

            if st.button("Remover pré-requisito"):
                codigo_origem, codigo_destino = opcoes[selecao]

                try:
                    resultado = remover_pre_requisito(
                        codigo_origem,
                        codigo_destino
                    )

                    if resultado:
                        st.session_state["mensagem_sucesso_pre"] = (
                            "Relacionamento removido com sucesso!"
                        )
                        st.rerun()
                    else:
                        st.warning("Relacionamento não encontrado.")

                except Exception as erro:
                    st.error(str(erro))
        else:
            st.info("Não existem relacionamentos cadastrados.")
