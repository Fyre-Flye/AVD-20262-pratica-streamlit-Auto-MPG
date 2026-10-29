# Declaração de Uso de IA

**Nome:** Gustavo Henrique Cruz de Oliveira
**Data:** 27/10/2026 (trabalho feito entre 22/10 e 27/10/2026)

## Ferramenta

Claude Code (CLI da Anthropic), com o modelo Claude Sonnet 5.5.

## Prompt usado

Os pedidos foram feitos em sequência, em português. Eles estão resumidos abaixo, na ordem em que foram enviados (alguns estão quase como escritos):

1. "execute os procedimentos de instalação e inicialização deste projeto"
2. "adapte o projeto para o meu notebook, mpg-auto, ele se encontra em uma pasta anterior a essa chamada EDA_AVD, salve em notebooks com o nome eda_original-user.ipynb, crie uma cópia do arquivo acima e cole as células de download de eda-com-downloads.ipynb [...] em resumo o projeto streamlit precisa rodar com meu notebook e dataset aparentemente"
3. "execute agora o streamlit"
4. "faça o rascunho de dashboard apresentado pela professora, em prompts" e, em seguida, "sim, faça" (rascunho do Dashboard 2 e preenchimento do template de prompt)
5. "certo, gere o dashboard agora" e depois "páginas separadas"
6. "Faça commits separados pelas features que a gente fez. Antes de commitar me diga como você planeja fazer isso." e depois "commite e dê push em um de cada vez. Sem coautoria sua. Há commits do repo da professora, sincronize o projeto antes, evite conflitos que vão vir da origem."
7. "pode usar as cores dela. Siga as alterações dela."
8. "preencha a justificativa das métricas" e a correção do heatmap, que mostrava só `mpg` e `weight` nos rótulos
9. "preencha a declaração de uso de IA e, como os nomes estão em inglês, se possível em parênteses ponha a tradução do termo." e, depois, "traduza todos os termos para português nessa aplicação" e "se puder use o sistema internacional de medida"
10. "faça um pequeno glossário (em tabela, duas colunas, termo e significado) em cada dashboard", com os ajustes "faça uma tabela menor, embaixo da correlação de Spearman. Frases curtas" e "eu falei só os termos de domínio, domínio automotivo"
11. "volte com nossa identidade visual anterior"
12. "escreva brevemente como se lê a correlação de Spearman abaixo do gráfico dele", depois o pedido de usar o azul e o vermelho das nossas cores nessas palavras e de um parágrafo de exemplo, e por fim "deixa, tire a interpretação"
13. "onde posso procurar novas identidades visuais pela internet?", "procure pela identidade da Chevron para começar" e "teste essa paleta no app"
14. "use cavalo de potência para potência do motor"
15. Sobre a leitura dos histogramas: "faça o 1" (tooltip com a faixa de valores) e, depois, a zona de hover na altura inteira de cada faixa e "uma linha dashed vertical por cada eixo, pra dar uma impressão de cursor"
16. "commite tudo separado por mudança, assim como fizemos e pode dar push" e a inclusão da pasta `slides/` ("os slides são nossos, eu que botei, pode subir também")

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
  - Os gráficos foram reescritos de Plotly para Altair e inicialmente passaram a usar as cores do tema dela (rosa claro e vermelho `#c1121f`), conforme pedi que seguíssemos as alterações dela. Depois pedi para voltar à nossa identidade visual anterior (laranja `#e8742a` e roxo `#2d223a`), e o `.streamlit/config.toml` foi restaurado à versão anterior.
  - O heatmap teve os rótulos do eixo inclinados em 45°, porque na coluna estreita alguns eram escondidos e só `mpg` e `weight` apareciam.
  - Os nomes das variáveis, que estão em inglês, foram traduzidos para português nos dashboards (ex.: `horsepower` aparece como "Potência"), a pedido meu.
  - As unidades foram convertidas para o Sistema Internacional (km/L, cm³, kg) no `src/data_loader.py`, a pedido meu; depois pedi que a potência ficasse em cavalos de potência (hp), como no dataset; o CSV tratado e o notebook continuam nas unidades originais, e a justificativa das métricas foi atualizada com os novos valores.
  - O glossário de cada dashboard foi reduzido a frases curtas e limitado aos termos do domínio automotivo do dataset; no Dashboard 1 ele fica embaixo do heatmap de Spearman.
  - O heatmap ganhou uma legenda curta "Como ler" abaixo dele, com as palavras "vermelho" e "azul" nas mesmas cores da escala do gráfico.
  - Testei uma paleta inspirada na Chevron (azul `#0056A2` e vermelho escuro `#9D1A36`, a partir de códigos de sites de terceiros), mas não gostei e a substituí.
  - A paleta atual é a da identidade visual "Altair Brand Identity Design" (Behance). A IA não conseguiu abrir a página (erro 403), então salvei um print da paleta em `media/altair-color.png` e a IA leu as cores da imagem: azul-escuro `#003075` (Nacional e correlação negativa), azul-claro `#0094FF` (Importado e correlação positiva) e `#F8F9F4` (neutro do heatmap). É só inspiração de cores, sem usar logo nem marca. Como a paleta não tem vermelho, a legenda "Como ler" passou a usar "azul-claro" e "azul-escuro".
  - As linhas Nacional e Importado do tooltip dos histogramas ganharam fundo na cor de cada classe, com letra em branco claro (`#F8F9F4`), via CSS, pois o tooltip do Vega não aceita cor por linha. O mesmo estilo vale para a legenda de Origem, para as palavras "azul-claro" e "azul-escuro" do "Como ler" e para os números do heatmap, a meu pedido, porque o texto colorido sem fundo ficava difícil de ler. Também pedi o ajuste do alinhamento e do tamanho dessas etiquetas, a partir de um print do tooltip.
  - Os histogramas ganharam tooltip com a faixa de valores de cada barra, uma zona de hover na altura inteira da faixa (porque algumas barras eram baixas demais para o mouse) e uma linha tracejada vertical que acompanha o mouse, a meu pedido.
  - A potência ficou em cavalos de potência (hp) e as demais unidades no Sistema Internacional (km/L, cm³ e kg).
  - A pasta `slides/` com os PDFs das aulas 21 e 22, que eu mesmo adicionei, foi incluída no repositório.
  - O histograma deixou de ser um selectbox com uma variável só e virou uma grade com um histograma por variável selecionada, como na implementação de referência da professora.

  - Depois da Aula 23, a IA conferiu o repositório contra o checklist dos slides. A partir disso, pedi para: adicionar mais dois visuais ao Dashboard 2 (gráfico de linha do consumo médio por ano e dispersão peso × consumo), para chegar a 3 visuais além das 4 métricas; trocar as páginas separadas por abas (`st.tabs`), como a professora sugere; e fazer o resto das pendências (`requirements.txt` com `altair` no lugar do `plotly`, que não é mais usado, `notebooks/eda.ipynb` com o meu notebook no lugar do placeholder e texto da justificativa dos novos visuais). Com as abas, os filtros dos dois dashboards ficam juntos na sidebar, com o nome do dashboard no título.
  - O deploy no Streamlit Community Cloud é feito por mim, com a minha conta do GitHub.

- **Rejeitado:**
  - A primeira versão em Plotly, trocada por Altair (preferido pela professora no Dashboard 1 e esperado no Dashboard 2).
  - Os dois dashboards na mesma página, que a IA tinha feito no início. Pedi páginas separadas e depois, a partir da Aula 23, mudei para abas (`st.tabs`), como a professora sugere.
  - Os `# TODO` originais do esqueleto, que foram implementados e removidos.
  - Um primeiro gráfico de barras com um eixo único, descartado porque `weight` tem escala muito maior que `mpg` e `horsepower` e achatava as barras; ficou um painel por variável.
  - O parágrafo de exemplo que interpretava o heatmap de Spearman (relações entre consumo, peso, cilindrada, potência e aceleração), que a IA escreveu e eu pedi para retirar.
  - A primeira versão do glossário, com termos de estatística e de interface (Spearman, histograma, intervalo etc.), que a IA incluiu e eu pedi para limitar ao domínio automotivo.
  - A coautoria da IA nos commits, que pedi para não incluir.

**Limitação:** a IA não teve acesso às instruções escritas no quadro pela professora, só aos arquivos do repositório. Onde algo parecia inconsistente, ela inferiu o que fazer e avisou, e eu revisei. A IA também não conseguiu abrir o app no navegador para conferir o resultado visualmente; as conferências foram feitas por testes automatizados do Streamlit e por imagens dos gráficos geradas fora do app.
