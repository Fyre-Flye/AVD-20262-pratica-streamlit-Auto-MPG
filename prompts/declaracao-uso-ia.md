# Declaração de Uso de IA

**Nome:** Gustavo Henrique Cruz de Oliveira
**Data:** 27/10/2026 (trabalho feito entre 22/10 e 27/10/2026)

## Ferramenta

Claude Code (CLI da Anthropic), com o modelo Claude Sonnet 5.5.

## Prompt usado

Os pedidos foram feitos em sequência, em português. Eles estão resumidos abaixo, na ordem em que foram enviados (o primeiro e os dois últimos estão quase como escritos):

1. "execute os procedimentos de instalação e inicialização deste projeto"
2. "adapte o projeto para o meu notebook, mpg-auto, ele se encontra em uma pasta anterior a essa chamada EDA_AVD, salve em notebooks com o nome eda_original-user.ipynb, crie uma cópia do arquivo acima e cole as células de download de eda-com-downloads.ipynb [...] em resumo o projeto streamlit precisa rodar com meu notebook e dataset aparentemente"
3. "execute agora o streamlit"
4. "faça o rascunho de dashboard apresentado pela professora, em prompts" e, em seguida, "sim, faça" (rascunho do Dashboard 2 e preenchimento do template de prompt)
5. "certo, gere o dashboard agora" e depois "páginas separadas"
6. "Faça commits separados pelas features que a gente fez. Antes de commitar me diga como você planeja fazer isso." e depois "commite e dê push em um de cada vez. Sem coautoria sua. Há commits do repo da professora, sincronize o projeto antes, evite conflitos que vão vir da origem."
7. "pode usar as cores dela. Siga as alterações dela."
8. "preencha a justificativa das métricas" e a correção do heatmap, que mostrava só `mpg` e `weight` nos rótulos
9. "preencha a declaração de uso de IA e, como os nomes estão em inglês, se possível em parênteses ponha a tradução do termo."

O template do prompt de rascunho → esqueleto está preenchido em [layout-skeleton-prompt.md](layout-skeleton-prompt.md), e os rascunhos estão em [../entregas/](../entregas/).

## O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:**
  - Criação do `.venv` e instalação das dependências seguindo o README (o `streamlit skills` caiu em instalação global, porque o Windows não permite symlinks sem Modo Desenvolvedor).
  - Cópia do meu notebook de EDA para `notebooks/eda_original-user.ipynb` e uma segunda cópia com as células de download adaptadas do `eda-com-downloads.ipynb` (geram `data/raw/` e `data/clean/`), sem alterar a minha análise.
  - Estrutura dos dashboards: heatmap de correlação de Spearman (a mesma escolha da EDA, já que nenhuma variável passou no teste de normalidade), histogramas, KPIs e gráfico de comparação por origem.
  - Texto da justificativa das métricas, com os números calculados sobre o dataset tratado.
  - Divisão do trabalho em commits separados por funcionalidade.

- **Modificado:**
  - O layout do Dashboard 1 segue o rascunho da professora; o do Dashboard 2 não tinha rascunho dela e foi proposto pela IA (4 KPIs no topo e gráfico por origem abaixo), por isso precisa da minha revisão.
  - Depois do `git merge` com o repositório da professora, os rascunhos passaram de `prompts/` para `entregas/`, com nomes com hífen, seguindo a nova estrutura dela.
  - Os gráficos foram reescritos de Plotly para Altair e passaram a usar as cores do tema dela (rosa claro e vermelho `#c1121f`), conforme pedi que seguíssemos as alterações dela.
  - O heatmap teve os rótulos do eixo inclinados em 45°, porque na coluna estreita alguns eram escondidos e só `mpg` e `weight` apareciam.
  - Os nomes das variáveis, que estão em inglês, ganharam a tradução entre parênteses nos dashboards (ex.: `horsepower (potência)`).
  - O histograma deixou de ser um selectbox com uma variável só e virou uma grade com um histograma por variável selecionada, como na implementação de referência da professora.

- **Rejeitado:**
  - A primeira versão em Plotly, trocada por Altair (preferido pela professora no Dashboard 1 e esperado no Dashboard 2).
  - Os dois dashboards na mesma página, que a IA tinha feito no início. Pedi páginas separadas, e a professora sugere abas (`st.tabs`), mas segui a minha escolha e usei páginas.
  - Os `# TODO` originais do esqueleto, que foram implementados e removidos.
  - Um primeiro gráfico de barras com um eixo único, descartado porque `weight` tem escala muito maior que `mpg` e `horsepower` e achatava as barras; ficou um painel por variável.
  - A coautoria da IA nos commits, que pedi para não incluir.

**Limitação:** a IA não teve acesso às instruções escritas no quadro pela professora, só aos arquivos do repositório. Onde algo parecia inconsistente, ela inferiu o que fazer e avisou, e eu revisei. A IA também não conseguiu abrir o app no navegador para conferir o resultado visualmente; as conferências foram feitas por testes automatizados do Streamlit e por imagens dos gráficos geradas fora do app.
