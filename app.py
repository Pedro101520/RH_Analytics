import streamlit as st
from paginas.visao_geral import visao
import pandas

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "inicio"

with st.sidebar:
    st.write("### Navegação entre Páginas")
    st.divider()
    st.button("Visão Geral", use_container_width=True)



if st.session_state.page == "inicio":
    visao()