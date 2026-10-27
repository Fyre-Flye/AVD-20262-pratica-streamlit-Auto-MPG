import pandas as pd
import plotly.express as px
import streamlit as st

from src.config import CORES_ORIGEM, VARS_QUANT
from src.data_loader import load_data

st.title("Dashboard 1 — Correlação e Distribuição")

df = load_data()

# Sidebar: filtros (variáveis + intervalo)
with st.sidebar:
    st.header("Filtros")

    variaveis = st.multiselect(
        "Variáveis Quantitativas",
        options=VARS_QUANT,
        default=VARS_QUANT,
        help="Selecione as variáveis quantitativas que deseja analisar no dashboard.",
    )

    separar_por_classe = st.toggle(
        "Distinguir por Classe",
        value=False,
        help="Colore a distribuição pela classe (origem: Nacional ou Importado).",
    )

    # Um slider de intervalo para cada variável selecionada
    intervalos = {}
    for var in variaveis:
        if pd.api.types.is_integer_dtype(df[var]):
            minimo, maximo, passo = int(df[var].min()), int(df[var].max()), 1
        else:
            minimo, maximo, passo = float(df[var].min()), float(df[var].max()), 0.1
        intervalos[var] = st.slider(
            f"Intervalo de {var}",
            min_value=minimo,
            max_value=maximo,
            value=(minimo, maximo),
            step=passo,
            key=f"intervalo_{var}",
        )

# Mantém só os carros dentro de todos os intervalos escolhidos
df_filtrado = df
for var, (inicio, fim) in intervalos.items():
    df_filtrado = df_filtrado[df_filtrado[var].between(inicio, fim)]

st.caption(f"{len(df_filtrado)} de {len(df)} carros dentro dos intervalos escolhidos.")

# Dashboard 1: correlação (heatmap) à esquerda, distribuição (histograma) à direita
col_correlacao, col_distribuicao = st.columns([1, 1.5])

with col_correlacao:
    st.subheader("Correlação")

    if len(variaveis) < 2:
        st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
    else:
        # Spearman, como na EDA: nenhuma variável passou no teste de normalidade
        matriz_corr = df_filtrado[variaveis].corr(method="spearman")
        fig_corr = px.imshow(
            matriz_corr,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            aspect="auto",
        )
        fig_corr.update_layout(margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig_corr, width="stretch")

with col_distribuicao:
    st.subheader("Distribuição")

    if not variaveis:
        st.warning("Selecione pelo menos 1 variável para ver a distribuição.")
    else:
        var_hist = st.selectbox("Variável do histograma", options=variaveis)
        fig_hist = px.histogram(
            df_filtrado,
            x=var_hist,
            color="origem" if separar_por_classe else None,
            color_discrete_map=CORES_ORIGEM,
            barmode="overlay",
            opacity=0.75,
            marginal="box",
        )
        fig_hist.update_layout(margin=dict(t=10, b=10, l=10, r=10), yaxis_title="Quantidade de carros")
        st.plotly_chart(fig_hist, width="stretch")
