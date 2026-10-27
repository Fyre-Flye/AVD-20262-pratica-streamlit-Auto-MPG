import pandas as pd
import streamlit as st

# O dataset original usa unidades imperiais; o app exibe tudo no Sistema Internacional (SI).
# coluna: (fator de conversão, casas decimais após converter)
CONVERSOES_SI = {
    "mpg": (0.425144, 2),          # milhas por galão (EUA) -> km/L
    "displacement": (16.387064, 0),  # polegadas cúbicas -> cm³
    "horsepower": (0.7457, 1),     # hp -> kW
    "weight": (0.45359237, 0),     # libras -> kg
}


@st.cache_data
def load_data(path="data/clean/dataset.csv"):
    """Lê o dataset já tratado (exportado ao final do notebook de EDA) e converte as unidades para o SI."""
    df = pd.read_csv(path)
    for coluna, (fator, casas) in CONVERSOES_SI.items():
        df[coluna] = (df[coluna] * fator).round(casas)
        if casas == 0:
            df[coluna] = df[coluna].astype(int)
    return df
