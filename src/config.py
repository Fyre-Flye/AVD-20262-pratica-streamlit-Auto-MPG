"""Constantes compartilhadas pelos dashboards (mesmas listas do notebook de EDA)."""

import altair as alt

VARS_QUANT = ["mpg", "displacement", "horsepower", "weight", "acceleration"]

# Nomes das colunas (em inglês) com a tradução entre parênteses, para exibir nos dashboards
ROTULOS = {
    "mpg": "mpg (milhas por galão)",
    "displacement": "displacement (cilindrada)",
    "horsepower": "horsepower (potência)",
    "weight": "weight (peso)",
    "acceleration": "acceleration (aceleração)",
}

# Cores em tons de sangue, iguais às do tema (.streamlit/config.toml): rosa claro para Nacional,
# vermelho arterial para Importado
COR_NACIONAL = "#f4a6a6"
COR_IMPORTADO = "#c1121f"
COR_HISTOGRAMA = COR_IMPORTADO
CORES_ORIGEM = alt.Scale(domain=["Nacional", "Importado"], range=[COR_NACIONAL, COR_IMPORTADO])

# Legenda da origem em texto, para caber no espaço livre da grade de histogramas
LEGENDA_ORIGEM = (
    f"**Origem**  \n"
    f":color[■]{{foreground=\"{COR_NACIONAL}\"}} Nacional  \n"
    f":color[■]{{foreground=\"{COR_IMPORTADO}\"}} Importado"
)
