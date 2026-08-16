import streamlit as st
from paginas.visao_geral import pag_visao
from paginas.rotatividade import pag_rotatividade

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "inicio"

with st.sidebar:
    st.write("### Navegação entre Páginas")
    st.divider()
    if st.button("Visão Geral", use_container_width=True):
        st.session_state.page = "inicio"
    if st.button("Taxa de rotatividade", use_container_width=True):
        st.session_state.page = "rotatividade"


if st.session_state.page == "inicio":
    pag_visao()
elif st.session_state.page == "rotatividade":
    pag_rotatividade()