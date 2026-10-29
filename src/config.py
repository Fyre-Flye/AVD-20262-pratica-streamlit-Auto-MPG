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

# Legenda da origem em texto, para caber no espaço livre da grade de histogramas
LEGENDA_ORIGEM = (
    f"**Origem**  \n"
    f":color[■]{{foreground=\"{COR_NACIONAL}\"}} Nacional  \n"
    f":color[■]{{foreground=\"{COR_IMPORTADO}\"}} Importado"
)
