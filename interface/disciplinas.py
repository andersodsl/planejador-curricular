
import streamlit as st

from services.disciplinas import (
    cadastrar_disciplina,
    buscar_disciplina,
    atualizar_disciplina,
    excluir_disciplina
)


def render(disciplinas):

    if "mensagem_sucesso" in st.session_state:
        st.success(st.session_state["mensagem_sucesso"])
        del st.session_state["mensagem_sucesso"]

    st.header("Gerenciamento de disciplinas")

    aba_cadastro, aba_consulta, aba_edicao, aba_exclusao = st.tabs(
        ["Cadastrar", "Consultar", "Editar", "Excluir"],
        key="disciplinas_tabs",
        on_change="rerun"
    )

    with aba_cadastro:
        st.subheader("Cadastrar nova disciplina")

        with st.form("form_cadastro"):
            nome = st.text_input("Nome da disciplina")
            codigo = st.text_input("Código da disciplina")

            periodo = st.number_input(
                "Período",
                min_value=1,
                step=1
            )

            carga_horaria = st.number_input(
                "Carga horária",
                min_value=1,
                step=1
            )

            descricao = st.text_area("Descrição")

            enviar = st.form_submit_button("Cadastrar disciplina")

            if enviar:
                try:
                    cadastrar_disciplina(
                        nome=nome,
                        codigo=codigo,
                        periodo=int(periodo),
                        carga_horaria=int(carga_horaria),
                        descricao=descricao
                    )

                    st.session_state["mensagem_sucesso"] = (
                        "Disciplina cadastrada com sucesso!"
                    )
                    st.rerun()

                except Exception as erro:
                    st.error(str(erro))

    with aba_consulta:
        st.subheader("Consultar disciplinas")

        if disciplinas:
            for disciplina in disciplinas:
                with st.expander(
                    f"{disciplina['codigo']} - {disciplina['nome']}"
                ):
                    st.write(f"**Código:** {disciplina['codigo']}")
                    st.write(f"**Nome:** {disciplina['nome']}")
                    st.write(f"**Período:** {disciplina['periodo']}")
                    st.write(
                        f"**Carga horária:** "
                        f"{disciplina['carga_horaria']} horas"
                    )
                    st.write(
                        f"**Descrição:** "
                        f"{disciplina.get('descricao', '')}"
                    )
        else:
            st.info("Nenhuma disciplina cadastrada.")

    with aba_edicao:
        st.subheader("Editar disciplina")

        if disciplinas:
            codigos = [
                disciplina["codigo"]
                for disciplina in disciplinas
            ]

            codigo_edicao = st.selectbox(
                "Selecione a disciplina:",
                codigos,
                key="codigo_edicao"
            )

            disciplina = buscar_disciplina(codigo_edicao)

            if disciplina:
                with st.form("form_edicao"):
                    novo_nome = st.text_input(
                        "Nome",
                        value=disciplina["nome"]
                    )

                    novo_periodo = st.number_input(
                        "Período",
                        min_value=1,
                        value=int(disciplina["periodo"]),
                        step=1
                    )

                    nova_carga = st.number_input(
                        "Carga horária",
                        min_value=1,
                        value=int(disciplina["carga_horaria"]),
                        step=1
                    )

                    nova_descricao = st.text_area(
                        "Descrição",
                        value=disciplina.get("descricao", "")
                    )

                    salvar = st.form_submit_button("Salvar alterações")

                    if salvar:
                        try:
                            atualizar_disciplina(
                                codigo=codigo_edicao,
                                nome=novo_nome,
                                periodo=int(novo_periodo),
                                carga_horaria=int(nova_carga),
                                descricao=nova_descricao
                            )

                            st.success(
                                "Disciplina atualizada com sucesso!"
                            )

                        except Exception as erro:
                            st.error(str(erro))
        else:
            st.info("Cadastre uma disciplina antes de editar.")

    with aba_exclusao:
        st.subheader("Excluir disciplina")

        if disciplinas:
            codigos = [
                disciplina["codigo"]
                for disciplina in disciplinas
            ]

            codigo_exclusao = st.selectbox(
                "Selecione a disciplina",
                codigos,
                key="codigo_exclusao"
            )

            if st.button("Excluir disciplina"):
                try:
                    resultado = excluir_disciplina(codigo_exclusao)

                    if resultado:
                        st.session_state["mensagem_sucesso"] = (
                            "Disciplina excluída com sucesso!"
                        )
                        st.rerun()
                    else:
                        st.error("Disciplina não encontrada.")

                except Exception as erro:
                    st.error(str(erro))
        else:
            st.info("Nenhuma disciplina cadastrada.")
