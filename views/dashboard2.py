import altair as alt
import pandas as pd
import streamlit as st

from src.config import CORES_ORIGEM, ROTULOS
from src.data_loader import load_data

st.title("Dashboard 2 — Indicadores (KPIs)")

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
    k2.metric("Consumo médio", f"{df_kpi['mpg'].mean():.1f} km/L".replace(".", ","))
    k3.metric("Potência média", f"{df_kpi['horsepower'].mean():.0f} kW")
    k4.metric("Peso médio", f"{df_kpi['weight'].mean():,.0f} kg".replace(",", "."))

    st.subheader("Comparação por origem")
    medias = df_kpi.groupby("origem")[["mpg", "horsepower", "weight"]].mean().reset_index()
    medias = medias.melt(id_vars="origem", var_name="variavel", value_name="media")
    medias["variavel"] = medias["variavel"].map(ROTULOS)
    # weight tem escala muito maior que mpg/horsepower: um painel por variável, eixo livre
    barras = (
        alt.Chart(medias)
        .mark_bar()
        .encode(
            x=alt.X("origem:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("media:Q", title="Média"),
            color=alt.Color("origem:N", title="Origem", scale=CORES_ORIGEM, legend=None),
            tooltip=[alt.Tooltip("origem", title="Origem"), alt.Tooltip("media:Q", title="Média", format=".1f")],
        )
        .properties(width=220, height=260)
    )
    rotulos = barras.mark_text(dy=-8).encode(text=alt.Text("media:Q", format=".1f"), color=alt.value("black"))
    grafico = (barras + rotulos).facet(column=alt.Column("variavel:N", title=None)).resolve_scale(y="independent")
    st.altair_chart(grafico, alt="Médias de consumo (km/L), potência (kW) e peso (kg) por origem (Nacional e Importado)")


# Glossário dos termos usados neste dashboard
st.divider()
st.caption("Glossário")
st.table(
    pd.DataFrame(
        [
            ("KPI (indicador)", "Número-resumo, como as médias do topo."),
            ("Total de carros", "Carros que passam nos filtros."),
            ("Consumo médio", "Média de km rodados por litro. Maior = mais econômico."),
            ("Potência média", "Média da força dos motores."),
            ("Peso médio", "Média da massa dos carros."),
            ("Origem", "Nacional: EUA. Importado: Europa e Japão."),
            ("Ano do modelo", "Ano de fabricação, de 1970 a 1982."),
            ("Comparação por origem", "Média de cada variável, Nacional contra Importado."),
        ],
        columns=["Termo", "Significado"],
    ).set_index("Termo")
)
