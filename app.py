import streamlit as st

from views import dashboard1, dashboard2

st.set_page_config(page_title="Auto MPG", layout="wide")

st.title("Auto MPG")

aba1, aba2 = st.tabs(["Dashboard 1 — Correlação e Distribuição", "Dashboard 2 — Indicadores (KPIs)"])

# Os filtros de cada dashboard ficam na sidebar, com o nome do dashboard no título
with aba1:
    dashboard1.render()
with aba2:
    dashboard2.render()
