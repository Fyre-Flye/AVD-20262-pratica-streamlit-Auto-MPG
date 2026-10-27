import plotly.express as px
import streamlit as st

from src.config import CORES_ORIGEM
from src.data_loader import load_data

st.title("Dashboard 2 — KPIs")

df = load_data()

with st.sidebar:
    st.header("Filtros")
    origens = st.multiselect(
        "Origem",
        options=["Nacional", "Importado"],
        default=["Nacional", "Importado"],
        help="Nacional = EUA; Importado = Europa + Japão.",
    )
    ano_min, ano_max = int(df["model_year"].min()), int(df["model_year"].max())
    anos = st.slider("Ano do modelo", ano_min, ano_max, (ano_min, ano_max))

df_kpi = df[df["origem"].isin(origens) & df["model_year"].between(*anos)]

if df_kpi.empty:
    st.warning("Nenhum carro para a origem e o ano escolhidos.")
else:
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total de carros", f"{len(df_kpi)}")
    k2.metric("mpg médio", f"{df_kpi['mpg'].mean():.1f}")
    k3.metric("Potência média", f"{df_kpi['horsepower'].mean():.0f} cv")
    k4.metric("Peso médio", f"{df_kpi['weight'].mean():,.0f} lb".replace(",", "."))

    st.subheader("Comparação por origem")
    medias = df_kpi.groupby("origem")[["mpg", "horsepower", "weight"]].mean().reset_index()
    medias = medias.melt(id_vars="origem", var_name="variavel", value_name="media")
    # weight tem escala muito maior que mpg/horsepower: um painel por variável, eixo livre
    fig_bar = px.bar(
        medias,
        x="origem",
        y="media",
        color="origem",
        facet_col="variavel",
        color_discrete_map=CORES_ORIGEM,
        text_auto=".1f",
    )
    fig_bar.update_yaxes(matches=None, showticklabels=True)
    fig_bar.update_layout(showlegend=False, margin=dict(t=30, b=10, l=10, r=10))
    st.plotly_chart(fig_bar, width="stretch")
