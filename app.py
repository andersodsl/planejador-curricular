import streamlit as st

from services.disciplinas import listar_disciplinas

from interface.visao_geral import render as render_visao_geral
from interface.disciplinas import render as render_disciplinas
from interface.pre_requisitos import render as render_pre_requisitos
from interface.grafo import render as render_grafo


# CONFIGURAÇÃO
st.set_page_config(
    page_title="Planejador de Grade Curricular",
    page_icon="📚",
    layout="wide"
)


# CABEÇALHO
st.title("📚 Planejador de Grade Curricular")

st.caption(
    "Sistema de gerenciamento de disciplinas e pré-requisitos acadêmicos."
)

st.divider()


# MENU
pagina = st.sidebar.radio(
    "Navegação",
    [
        "Visão geral",
        "Disciplinas",
        "Pré-requisitos",
        "Grafo de pré-requisitos"
    ]
)


# CARREGAMENTO
try:
    disciplinas = listar_disciplinas()

except Exception as erro:
    st.error(f"Erro ao carregar o banco de dados: {erro}")
    st.stop()


# NAVEGAÇÃO
if pagina == "Visão geral":
    render_visao_geral(disciplinas)

elif pagina == "Disciplinas":
    render_disciplinas(disciplinas)

elif pagina == "Pré-requisitos":
    render_pre_requisitos(disciplinas)

elif pagina == "Grafo de pré-requisitos":
    render_grafo(disciplinas)