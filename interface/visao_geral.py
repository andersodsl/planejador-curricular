
import streamlit as st


def render(disciplinas):
    st.header("Visão geral do sistema")

    total_disciplinas = len(disciplinas)

    periodos = {
        disciplina["periodo"]
        for disciplina in disciplinas
    }

    carga_total = sum(
        disciplina["carga_horaria"]
        for disciplina in disciplinas
    )

    coluna1, coluna2, coluna3 = st.columns(3)

    coluna1.metric(
        "Disciplinas cadastradas",
        total_disciplinas
    )

    coluna2.metric(
        "Períodos identificados",
        len(periodos)
    )

    coluna3.metric(
        "Carga horária total",
        f"{carga_total} h"
    )

    st.divider()

    st.subheader("Disciplinas cadastradas")

    if disciplinas:
        dados = []

        for disciplina in disciplinas:
            dados.append({
                "Código": disciplina["codigo"],
                "Nome": disciplina["nome"],
                "Período": disciplina["periodo"],
                "Carga horária": disciplina["carga_horaria"]
            })

        st.dataframe(
            dados,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("Ainda não existem disciplinas cadastradas.")
