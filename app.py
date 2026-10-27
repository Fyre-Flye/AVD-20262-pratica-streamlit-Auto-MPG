import streamlit as st

st.set_page_config(page_title="Auto MPG", layout="wide")

pagina = st.navigation(
    [
        st.Page("views/dashboard1.py", title="Dashboard 1 — Correlação e Distribuição", icon=":material/scatter_plot:", default=True),
        st.Page("views/dashboard2.py", title="Dashboard 2 — Indicadores (KPIs)", icon=":material/speed:"),
    ]
)
pagina.run()
