# Justificativa das métricas — Dashboard 2

Dataset: Auto MPG (UCI), 392 carros de 1970 a 1982, após remover 6 linhas com `horsepower` ausente. Os KPIs reagem aos widgets do dashboard: **origem** (Nacional = EUA; Importado = Europa + Japão) e **ano do modelo**.

Público-alvo comum às métricas: pessoas que querem entender, de forma rápida, o perfil da frota e o consumo de combustível da época (ex.: quem analisa o mercado automotivo ou avalia políticas de eficiência), sem precisar ler histogramas ou matrizes de correlação.

## Métrica 1: Total de carros
- **Variável:** contagem de linhas do dataset (um carro por linha), após os filtros de origem e ano.
- **O que mede:** quantos carros fazem parte do recorte escolhido nos widgets (392 com todos os filtros abertos; 245 nacionais e 147 importados).
- **Por que foi escolhida:** é o contexto das demais métricas. Uma média calculada sobre poucos carros pesa menos do que sobre muitos, e o número deixa isso visível quando o filtro estreita o recorte.
- **Público-alvo:** o comum descrito acima.
- **Qual decisão pode ser apoiada por essa métrica?** Decidir se um recorte é grande o suficiente para tirar conclusões ou se as médias abaixo devem ser lidas com cautela.
- **O que comunica ao público-alvo:** o tamanho da amostra analisada (ex.: "há 245 carros nacionais, quase o dobro dos importados"), que também mostra o desbalanceamento entre as origens.

## Métrica 2: mpg médio
- **Variável:** `mpg` (milhas por galão, consumo de combustível).
- **O que mede:** a média de milhas que o carro percorre com um galão no recorte escolhido. Quanto maior, mais econômico (23,4 mpg no total; 29,1 nos importados; 20,0 nos nacionais).
- **Por que foi escolhida:** `mpg` (milhas por galão) é a variável de interesse do estudo e a que mais se relaciona com as demais (correlação de Spearman de cerca de -0,85 com `weight` (peso), `displacement` (cilindrada) e `horsepower` (potência)). Resume o desempenho de consumo em um único número.
- **Público-alvo:** o comum descrito acima.
- **Qual decisão pode ser apoiada por essa métrica?** Comparar a economia de combustível entre origens e entre anos, por exemplo para avaliar se a eficiência da frota melhorou ao longo do período.
- **O que comunica ao público-alvo:** o quão econômica é a frota em média, sem precisar interpretar a distribuição (ex.: "os importados andam cerca de 9 milhas a mais por galão").

## Métrica 3: Potência média
- **Variável:** `horsepower` (potência do motor, em cv).
- **O que mede:** a potência média dos motores no recorte (104 cv no total; 80 cv nos importados; 119 cv nos nacionais).
- **Por que foi escolhida:** potência está fortemente ligada ao consumo (quanto mais potente, menos econômico), então ajuda a explicar a métrica de `mpg`. Usamos a média, mesmo a variável sendo assimétrica à direita, porque o KPI precisa ser simples de ler; a mediana é menor (93,5 cv) e fica como ressalva.
- **Público-alvo:** o comum descrito acima.
- **Qual decisão pode ser apoiada por essa métrica?** Entender se uma diferença de consumo entre grupos vem do perfil de motor (mais potente ou mais modesto) antes de atribuí-la à origem.
- **O que comunica ao público-alvo:** o perfil de motor da frota recortada (ex.: "carros nacionais têm motores bem mais potentes, e isso tem um custo em consumo").

## Métrica 4: Peso médio
- **Variável:** `weight` (peso do carro, em libras).
- **O que mede:** o peso médio dos carros no recorte (2.978 lb no total; 2.319 lb nos importados; 3.372 lb nos nacionais).
- **Por que foi escolhida:** é a variável mais correlacionada com `mpg` (cerca de -0,88 em Spearman), então é o melhor indicador isolado do porte do carro. Complementa a potência: juntas descrevem "carro grande e potente" versus "carro leve e econômico".
- **Público-alvo:** o comum descrito acima.
- **Qual decisão pode ser apoiada por essa métrica?** Avaliar o efeito do porte dos carros sobre a eficiência da frota, por exemplo ao discutir a redução de peso como caminho para economizar combustível.
- **O que comunica ao público-alvo:** o porte típico dos carros da amostra (ex.: "os nacionais pesam cerca de 1.050 lb (uns 475 kg) a mais, em média, que os importados").

## Visual: Comparação por origem (gráfico de barras)
- **Variáveis:** `mpg` (milhas por galão), `horsepower` (potência) e `weight` (peso), agrupadas por `origem`.
- **O que mede:** a média de cada variável para carros Nacionais e Importados lado a lado, em um painel por variável (as escalas são muito diferentes, então cada painel tem o seu eixo).
- **Por que foi escolhido:** reúne as três métricas acima em uma só comparação visual, que responde à pergunta central do dashboard: o que diferencia carros nacionais e importados?
- **O que comunica ao público-alvo:** que os importados são mais leves, menos potentes e mais econômicos, e que o consumo acompanha o porte do carro. A comparação descreve a amostra e não prova que a origem é a causa; o estudo é observacional e os carros importados vendidos nos EUA da época eram, em geral, compactos.
