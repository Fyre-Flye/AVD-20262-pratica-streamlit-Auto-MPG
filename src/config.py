"""Constantes compartilhadas pelos dashboards (mesmas listas do notebook de EDA)."""

import altair as alt

VARS_QUANT = ["mpg", "displacement", "horsepower", "weight", "acceleration"]

# Nomes das colunas (em inglês) traduzidos, com a unidade do SI, para exibir nos dashboards
ROTULOS = {
    "mpg": "Consumo (km/L)",
    "displacement": "Cilindrada (cm³)",
    "horsepower": "Potência (hp)",
    "weight": "Peso (kg)",
    "acceleration": "Aceleração (s)",
}

# Paleta da identidade visual da Altair (Behance): azul-escuro para Nacional, azul-claro para Importado
AZUL_ESCURO = "#003075"
AZUL_CLARO = "#0094FF"
FUNDO_NEUTRO = "#F8F9F4"
COR_NACIONAL = AZUL_ESCURO
COR_IMPORTADO = AZUL_CLARO
COR_HISTOGRAMA = COR_NACIONAL

# Escala do heatmap de correlação: azul-escuro (negativa), neutro no zero, azul-claro (positiva)
ESCALA_CORRELACAO = alt.Scale(domain=[-1, 0, 1], range=[AZUL_ESCURO, FUNDO_NEUTRO, AZUL_CLARO])
CORES_ORIGEM = alt.Scale(domain=["Nacional", "Importado"], range=[COR_NACIONAL, COR_IMPORTADO])


# Texto com fundo na cor da classe e letra em branco claro, para ler em qualquer tema (HTML:
# o markdown de cor do Streamlit não garante o fundo, e st.caption deixa o texto desbotado)
def destaque(texto, cor):
    return (
        f'<span style="background:{cor}; color:{FUNDO_NEUTRO}; padding:0 0.4em; line-height:1.4; '
        f'border-radius:0.25em; font-weight:600; white-space:nowrap">{texto}</span>'
    )


# Legenda da origem numa linha só, com as etiquetas lado a lado e alinhadas ao centro
LEGENDA_ORIGEM = (
    '<div style="display:flex; align-items:center; gap:0.5em; font-size:0.9em">'
    "<strong>Origem</strong>"
    f"{destaque('Nacional', COR_NACIONAL)}"
    f"{destaque('Importado', COR_IMPORTADO)}"
    "</div>"
)
