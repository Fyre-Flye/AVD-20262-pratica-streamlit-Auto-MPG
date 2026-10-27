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

# TESTE de paleta inspirada na Chevron: azul para Nacional, vermelho escuro para Importado
AZUL = "#0056A2"
VERMELHO = "#9D1A36"
COR_NACIONAL = AZUL
COR_IMPORTADO = VERMELHO
COR_HISTOGRAMA = COR_NACIONAL
CORES_ORIGEM = alt.Scale(domain=["Nacional", "Importado"], range=[COR_NACIONAL, COR_IMPORTADO])

# Legenda da origem em texto, para caber no espaço livre da grade de histogramas
LEGENDA_ORIGEM = (
    f"**Origem**  \n"
    f":color[■]{{foreground=\"{COR_NACIONAL}\"}} Nacional  \n"
    f":color[■]{{foreground=\"{COR_IMPORTADO}\"}} Importado"
)
