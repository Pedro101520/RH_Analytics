import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

def pag_visao():
    df = pd.read_csv(r"DATA\HR_Analytics_Cleaned_Master.csv")

    st.title("Visão Geral")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        container = st.container(height=120, border=False)
        with container:
            st.caption("## Total de Funcionários: ")
        st.write(f"# {df.shape[0]}")
    with col2:
        container = st.container(height=120, border=False)
        with container:
            st.caption("## Taxa de rotatividade: ")
        df_demissao = df.query('Attrition == "Yes"')
        st.write(f"# {round((df_demissao.shape[0] / df.shape[0]), 3) * 100}%")
    with col3:
        container = st.container(height=120, border=False)
        with container:
            st.caption("## Idade média dos funcionários: ")
        st.write(f"# {round(df["Age"].mean(), 1)}")
    with col4:
        container = st.container(height=120, border=False)
        with container:
            st.caption("## Salário Médio: ")
        st.write(f"# {round(df["MonthlyIncome"].mean(), 2)}")

    st.divider()

    st.caption("## Funcionários por departamento: ")
    df_departamento = df["Department"].value_counts().reset_index()
    df_departamento.columns = ["Department", "funcionarios"]

    st.bar_chart(
        df_departamento,
        x="Department",
        y="funcionarios",
        horizontal=True,
        height=300
    )

    st.divider()

    st.caption("## Funcionários por cargo: ")
    df_cargo = df["JobRole"].value_counts().sort_values(ascending=True).reset_index()
    df_cargo.columns = ["JobRole", "funcionarios"]

    st.bar_chart(
        df_cargo,
        x="JobRole",
        y="funcionarios",
        horizontal=True,
        height=300
    )


