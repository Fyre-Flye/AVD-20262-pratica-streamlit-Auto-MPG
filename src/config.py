"""Constantes compartilhadas pelos dashboards (mesmas listas do notebook de EDA)."""

import altair as alt

VARS_QUANT = ["mpg", "displacement", "horsepower", "weight", "acceleration"]

# Nomes das colunas (em inglês) traduzidos, com a unidade do SI, para exibir nos dashboards
ROTULOS = {
    "mpg": "Consumo (km/L)",
    "displacement": "Cilindrada (cm³)",
    "horsepower": "Potência (kW)",
    "weight": "Peso (kg)",
    "acceleration": "Aceleração (s)",
}

# Identidade visual do projeto: laranja para Nacional, roxo escuro para Importado
COR_NACIONAL = "#e8742a"
COR_IMPORTADO = "#2d223a"
COR_HISTOGRAMA = COR_NACIONAL
CORES_ORIGEM = alt.Scale(domain=["Nacional", "Importado"], range=[COR_NACIONAL, COR_IMPORTADO])

# Legenda da origem em texto, para caber no espaço livre da grade de histogramas
LEGENDA_ORIGEM = (
    f"**Origem**  \n"
    f":color[■]{{foreground=\"{COR_NACIONAL}\"}} Nacional  \n"
    f":color[■]{{foreground=\"{COR_IMPORTADO}\"}} Importado"
)
