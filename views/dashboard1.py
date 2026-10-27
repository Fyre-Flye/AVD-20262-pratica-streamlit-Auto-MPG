import altair as alt
import pandas as pd
import streamlit as st

from src.config import COR_HISTOGRAMA, CORES_ORIGEM, LEGENDA_ORIGEM, ROTULOS, VARS_QUANT
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
        format_func=ROTULOS.get,
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
            f"Intervalo de {ROTULOS[var]}",
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

# Dashboard 1: correlação (heatmap) à esquerda, distribuição (histogramas) à direita
col_correlacao, col_distribuicao = st.columns([1, 1.5])

with col_correlacao:
    st.subheader("Correlação (Spearman)")

    if len(variaveis) < 2:
        st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
    elif len(df_filtrado) < 30:
        st.warning("Poucos carros nos intervalos escolhidos para calcular a correlação.")
    else:
        # Spearman, como na EDA (nenhuma variável passou no teste de normalidade), em formato longo
        corr = (
            df_filtrado[variaveis]
            .rename(columns=ROTULOS)
            .corr(method="spearman")
            .rename_axis(index="var_y", columns="var_x")
            .stack()
            .rename("correlacao")
            .reset_index()
        )
        # Só o triângulo inferior, sem a diagonal (sempre 1): a matriz é simétrica, o resto é repetição
        rotulos = [ROTULOS[var] for var in variaveis]
        ordem = {rotulo: i for i, rotulo in enumerate(rotulos)}
        corr = corr[corr["var_y"].map(ordem) > corr["var_x"].map(ordem)]

        base = alt.Chart(corr).encode(
            x=alt.X(
                "var_x:N",
                title=None,
                sort=rotulos[:-1],  # a última variável só aparece nas linhas
                axis=alt.Axis(labelAngle=-45, labelFontSize=13, labelOverlap=False),  # inclinado para não esconder rótulos
            ),
            y=alt.Y("var_y:N", title=None, sort=rotulos[1:], axis=alt.Axis(labelFontSize=14)),  # a primeira só nas colunas
        )
        heatmap = base.mark_rect().encode(
            color=alt.Color(
                "correlacao:Q",
                title="Spearman",
                scale=alt.Scale(scheme="redblue", domain=[-1, 1], reverse=True),
                legend=alt.Legend(orient="bottom", titleFontSize=14, labelFontSize=13),
            ),
            tooltip=["var_x", "var_y", alt.Tooltip("correlacao:Q", format=".2f")],
        )
        valores = base.mark_text(fontSize=16).encode(
            text=alt.Text("correlacao:Q", format=".2f"),
            color=alt.condition("abs(datum.correlacao) > 0.5", alt.value("white"), alt.value("black")),
        )

        st.altair_chart(
            (heatmap + valores).properties(height=380),
            width="stretch",
            alt="Mapa de calor (triângulo inferior, sem a diagonal) da correlação de Spearman entre as variáveis quantitativas selecionadas",
        )

with col_distribuicao:
    st.subheader("Distribuição")

    if not variaveis:
        st.warning("Selecione pelo menos 1 variável para ver a distribuição.")
    elif df_filtrado.empty:
        st.warning("Nenhum carro dentro dos intervalos escolhidos.")
    else:
        # Com número par de variáveis não sobra espaço na grade: a legenda vai acima dela
        if separar_por_classe and len(variaveis) % 2 == 0:
            st.markdown(LEGENDA_ORIGEM)

        # Um histograma por variável selecionada, em grade de 2 colunas (cada um com a sua escala)
        for inicio in range(0, len(variaveis), 2):
            colunas = st.columns(2)
            for coluna, var in zip(colunas, variaveis[inicio : inicio + 2]):
                histograma = (
                    alt.Chart(df_filtrado[[var, "origem"]])
                    .mark_bar()
                    .encode(
                        x=alt.X(f"{var}:Q", bin=alt.Bin(maxbins=20), title=ROTULOS[var]),
                        y=alt.Y("count()", title="Carros"),
                        tooltip=[alt.Tooltip("count()", title="Carros")],
                    )
                    .properties(height=200)
                )
                if separar_por_classe:
                    histograma = histograma.encode(
                        color=alt.Color("origem:N", title="Origem", scale=CORES_ORIGEM, legend=None),
                        tooltip=["origem", alt.Tooltip("count()", title="Carros")],
                    )
                else:
                    histograma = histograma.mark_bar(color=COR_HISTOGRAMA)

                with coluna:
                    st.altair_chart(histograma, width="stretch", alt=f"Histograma da variável {ROTULOS[var]}")

            # Número ímpar de variáveis: a legenda ocupa o espaço que sobrou na última linha
            if separar_por_classe and len(variaveis[inicio : inicio + 2]) == 1:
                colunas[1].markdown(LEGENDA_ORIGEM)
