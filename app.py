import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel("censo_1872.xlsx")
df = df.drop_duplicates()

path = "censo_1872.xlsx"

bruto = pd.read_excel(path)

indicador_1 = bruto.iloc[:].copy()
indicador_1.columns = [
    "Ano",
    "ID Província",
    "ID Município",
    "Homens livres",
    "Mulheres Livres",
    "Total Livres",
    "Homens Escravos",
    "Mulheres escravas",
    "Total escravizados",
    "Total",
]

# ---------------------PAGINA REAL---------------------

st.set_page_config(
    page_title="Censo 1872",
    layout="wide"
)

st.title("CENSO 1872")
st.header("Tabela")

st.dataframe(indicador_1)

st.text("Fonte: https://basedosdados.org/")

if "show_news" not in st.session_state:
    st.session_state.show_graphic = False

st.sidebar.header("PÁGINAS")
if st.sidebar.button("Gráficos"):
    st.session_state.show_graphic = True

if st.sidebar.button("Tabela"):
    st.session_state.show_graphic = False

if st.session_state.show_graphic:
# Tela de notícias
    st.title("Gráficos")