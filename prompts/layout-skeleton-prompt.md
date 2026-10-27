# Prompt: rascunho de layout → esqueleto do app

## Contexto

Sou aluno da disciplina Análise e Visualização de Dados (Cesar School, 2026.2). Estou construindo dois dashboards em Streamlit a partir da minha EDA do dataset **Auto MPG** (UCI, id=9), que já está tratado em `data/clean/dataset.csv` (392 carros; 6 linhas com `horsepower` ausente foram removidas). O objetivo é explorar o consumo (`mpg`) e suas relações com as demais características do carro.

- Dashboard 1: correlação + distribuição das variáveis quantitativas.
- Dashboard 2: KPIs.

## Entrada

Rascunhos de layout:

- Dashboard 1: `entregas/rascunho-dashboard1.png` (sidebar à esquerda; heatmap de correlação no centro; histograma à direita).
- Dashboard 2: `entregas/rascunho-dashboard2.png` (sidebar à esquerda; 4 KPIs no topo; gráfico de barras de comparação por origem abaixo).

Colunas do dataset: `mpg`, `cylinders`, `displacement`, `horsepower`, `weight`, `acceleration`, `model_year`, `origin` (1 = EUA, 2 = Europa, 3 = Japão), `car_name`, `origem` (Nacional = EUA, Importado = Europa + Japão).

Variáveis quantitativas: `mpg`, `displacement`, `horsepower`, `weight`, `acceleration`.

Perguntas que os dashboards devem responder:

1. Quais variáveis se correlacionam com o consumo (`mpg`) e entre si?
2. Como cada variável quantitativa se distribui, e isso muda entre carros nacionais e importados?
3. Qual o perfil médio da frota (total de carros, `mpg`, potência e peso médios) e como ele difere por origem?

## Restrições

- Usar apenas Streamlit e plotly (`px.imshow`, `px.histogram`, `px.bar`).
- Editar somente o `app.py`; carregar os dados via `src/data_loader.py` (`load_data()`), sem ler o CSV direto.
- Manter os filtros da sidebar já existentes (variáveis, intervalo e "Distinguir por Classe") e a coluna de classe `origem`.
- Todo gráfico e KPI deve usar o `df_filtrado`, para reagir aos filtros.
- Não calcular correlação com menos de 2 variáveis selecionadas (exibir aviso).
- Não alterar o dataset nem o notebook de EDA.

## Formato de saída

Esqueleto do `app.py` com os blocos de cada dashboard e comentários `# TODO` onde falta implementar, mais uma explicação breve de cada seção (uma ou duas linhas).
