import altair as alt
import pandas as pd
import streamlit as st

from src.config import AZUL, COR_HISTOGRAMA, COR_IMPORTADO, COR_NACIONAL, CORES_ORIGEM, ESCALA_CORRELACAO, LEGENDA_ORIGEM, ROTULOS, VARS_QUANT, VERMELHO
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

ALTURA_HISTOGRAMA = 200

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
                scale=ESCALA_CORRELACAO,
                legend=alt.Legend(orient="bottom", titleFontSize=14, labelFontSize=13),
            ),
            tooltip=[alt.Tooltip("var_x", title="Variável 1"), alt.Tooltip("var_y", title="Variável 2"), alt.Tooltip("correlacao:Q", title="Correlação", format=".2f")],
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
        st.caption(
            "**Como ler:** os valores vão de -1 a 1. "
            f"Perto de 1 (:color[**vermelho**]{{foreground=\"{VERMELHO}\"}}), as variáveis sobem juntas. "
            f"Perto de -1 (:color[**azul**]{{foreground=\"{AZUL}\"}}), uma sobe e a outra desce. "
            "Perto de 0, não há relação."
        )

    st.caption("Glossário")
    st.table(
        pd.DataFrame(
            [
                ("Consumo", "Km rodados por litro."),
                ("Cilindrada", "Volume do motor."),
                ("Potência", "Força do motor."),
                ("Peso", "Massa do carro."),
                ("Aceleração", "Tempo para acelerar. Maior = mais lento."),
                ("Origem", "Nacional: EUA. Importado: Europa e Japão."),
                ("Ano do modelo", "Ano de fabricação, de 1970 a 1982."),
            ],
            columns=["Termo", "Significado"],
        ).set_index("Termo")
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

        # O tooltip do Vega não aceita cor por linha; como a ordem das linhas é fixa (faixa, carros,
        # Nacional, Importado), a 3ª e a 4ª linhas são coloridas com a cor de cada classe.
        if separar_por_classe:
            st.html(
                f"<style>"
                f"#vg-tooltip-element tr:nth-child(3) td {{ color: {COR_NACIONAL} !important; }}"
                f"#vg-tooltip-element tr:nth-child(4) td {{ color: {COR_IMPORTADO} !important; }}"
                f"</style>"
            )

        # Um histograma por variável selecionada, em grade de 2 colunas (cada um com a sua escala)
        for inicio in range(0, len(variaveis), 2):
            colunas = st.columns(2)
            for coluna, var in zip(colunas, variaveis[inicio : inicio + 2]):
                divisao = alt.Bin(maxbins=20)
                histograma = (
                    alt.Chart(df_filtrado[[var, "origem"]])
                    .mark_bar()
                    .encode(
                        x=alt.X(f"{var}:Q", bin=divisao, title=ROTULOS[var]),
                        y=alt.Y("count()", title="Carros"),
                    )
                )
                if separar_por_classe:
                    histograma = histograma.encode(
                        color=alt.Color("origem:N", title="Origem", scale=CORES_ORIGEM, legend=None),
                    )
                else:
                    histograma = histograma.mark_bar(color=COR_HISTOGRAMA)

                # Camada invisível com a altura inteira do gráfico, POR CIMA das barras: o mouse é captado
                # em qualquer ponto da faixa, mesmo onde a barra é muito baixa. Ela calcula a faixa
                # (inicio–fim) e as contagens de cada faixa para o tooltip e para a linha de cursor.
                cursor = alt.selection_point(fields=["inicio"], on="pointerover", clear="pointerout", empty=False)
                por_faixa = (
                    alt.Chart(df_filtrado[[var, "origem"]])
                    .transform_bin(["inicio", "fim"], field=var, bin=divisao)
                    .transform_calculate(
                        faixa="format(datum.inicio, '~g') + ' – ' + format(datum.fim, '~g')",
                        e_nacional="datum.origem == 'Nacional' ? 1 : 0",
                        e_importado="datum.origem == 'Importado' ? 1 : 0",
                        meio="(datum.inicio + datum.fim) / 2",
                    )
                    .transform_joinaggregate(
                        total="count()", nacional="sum(e_nacional)", importado="sum(e_importado)", groupby=["inicio"]
                    )
                )
                dicas = [alt.Tooltip("faixa:N", title=ROTULOS[var]), alt.Tooltip("total:Q", title="Carros")]
                if separar_por_classe:
                    dicas += [alt.Tooltip("nacional:Q", title="Nacional"), alt.Tooltip("importado:Q", title="Importado")]

                zona_hover = (
                    por_faixa.mark_bar(opacity=0)
                    .encode(
                        x=alt.X("inicio:Q", title=ROTULOS[var]),
                        x2="fim:Q",
                        y=alt.value(0),
                        y2=alt.value(ALTURA_HISTOGRAMA),
                        tooltip=dicas,
                    )
                    .add_params(cursor)
                )
                # Linha tracejada vertical no meio da faixa sob o mouse, como um cursor
                linha_cursor = (
                    por_faixa.transform_filter(cursor)
                    .mark_rule(strokeDash=[5, 4], color="#555555")
                    .encode(x=alt.X("meio:Q", title=ROTULOS[var]))
                )
                grafico = alt.layer(histograma, linha_cursor, zona_hover).properties(height=ALTURA_HISTOGRAMA)

                with coluna:
                    st.altair_chart(grafico, width="stretch", alt=f"Histograma da variável {ROTULOS[var]}")

            # Número ímpar de variáveis: a legenda ocupa o espaço que sobrou na última linha
            if separar_por_classe and len(variaveis[inicio : inicio + 2]) == 1:
                colunas[1].markdown(LEGENDA_ORIGEM)

