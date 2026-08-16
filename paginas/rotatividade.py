import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

def pag_rotatividade():
    df = pd.read_csv(r"DATA\HR_Analytics_Cleaned_Master.csv")

    st.title("Análise de Rotatividade")

    df_demissao = df.query('Attrition == "Yes"')
    rotatividade = (round((df_demissao.shape[0] / df.shape[0]), 3) * 100)

    st.caption(f"## Taxa geral de rotatividade: {rotatividade}%")

    st.divider()

    st.caption("#### Taxa por departamento: ")

    df_rotatividade = df[(df["Attrition"] == "Yes")]["Department"].value_counts().reset_index()
    df_rotatividade.columns = ["Department", "demitidos"]
    
    df_departamento = df["Department"].value_counts().reset_index()
    df_departamento.columns = ["Department", "funcionarios"]

    df_rotatividade["taxa"] = round(df_rotatividade["demitidos"] / df_departamento["funcionarios"], 3)
    df_rotatividade["funcionarios"] = df_departamento["funcionarios"]

    fig = px.bar(
        df_rotatividade,
        x="taxa",
        y="Department",
        orientation="h",
        text=df_rotatividade["taxa"].map(lambda x: f"{x:.1%}"),
        hover_data={"demitidos": True, "funcionarios": True, "taxa": ":.1%"},
    )

    fig.update_layout(
        xaxis_tickformat=".0%",
        xaxis_title="Taxa de rotatividade",
        yaxis_title="Departamento",
        height=300,
    )
    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)
