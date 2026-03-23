# Projeto: Introdução à Ciência de Dados

**Integrantes:** Ricardo Morais Pistori, João Rafael Gadelha de Araújo, Victor Hugo Araújo de Vasconcelos, Kaio Vitor Santos de Lima

**Tema:** Uma breve análise sobre o desenvolvimento do mercado cinematográfico no Brasil (1997 - 2025).

---

## 2. Sobre o Conjunto de Dados

### 2.1 relacao_sala_publico e coleta_multiplex

O conjunto de dados mapeia a evolução histórica do mercado cinematográfico brasileiro. Ele abrange dados históricos, incluindo o total de salas disponíveis por ano e a relação de público médio por sala desde a década de 1970 até os anos recentes. Esses dados permitem analisar o ritmo de expansão do setor, o impacto da transição para os complexos multiplex e as flutuações de demanda do público ao longo das décadas.

### 2.2 bilheteria-diaria-obras-por-distribuidoras e bilheteria-diaria-obras-por-exibidoras

csvs contendo as bilheterias diárias das sessões de exibição do período de 2014 a 2025( bem como informações sobre o país de origem das obras  ) baseando-se, respectivamente, nos dados advindos das distribuidoras e das exibidoras dos filmes.

### 2.3 31072025_TabelasFSA

informações sobre o fundo setorial audiovisual(FSA), as planilhas contêm informações de 2007-2025, contendo,  arrecadação, execução orçamentária, empenhos, desembolsos, investimentos, financiamentos, apoios, despesas operacionais e saldo bancário do programa.

### 2.4 pmi_ancine

Preço médio dos ingressos de cinema dos anos 2002_2024.

### 2.5 quantidade_ano

Quantidade de filmes brasileiros produzidos ano a ano 1910-2024.

---

## 3 Processo de Coleta de Dados e descrição das colunas

### Relacao_sala_publico e coleta_multiplex

A coleta de dados foi realizada de forma automatizada através da técnica de *web scraping*, extraindo informações do portal especializado *Filme B*. Utilizando a linguagem Python, scripts foram desenvolvidos com o auxílio das bibliotecas **Selenium** (para automação e navegação web) e **Pandas** (para estruturação em DataFrames). 

O algoritmo localiza as tabelas HTML corretas usando filtros de texto e tamanho, extrai o código bruto e o converte para um formato tabular estruturado, salvando os resultados para análise.

#### Dicionário de Dados (Descrição das Colunas)

Abaixo estão descritas as principais colunas extraídas durante as rotinas de coleta de dados (multiplex e relação público/sala):

- **Nome da coluna:** `Ano`  
  - **Descrição da coluna:** Ano de referência do registro histórico dos dados.  
  - **Exemplo:** `2020`

- **Nome da coluna:** `Total_Salas`  
  - **Descrição da coluna:** O número total acumulado de salas multiplex em operação no Brasil durante o ano avaliado.  
  - **Exemplo:** `2757`

- **Nome da coluna:** `Média por Sala`  
  - **Descrição da coluna:** A média anual de espectadores (público) que frequentou cada sala de cinema no período especificado.  
  - **Exemplo:** `25000` *(Valor numérico contínuo referente à lotação média)*

---

### bilheteria-diaria-obras-por-distribuidoras e bilheteria-diaria-obras-por-exibidoras

os dados foram obtidos em um repositório de acesso público disponibilizado pela  
Agência Nacional do Cinema (ANCINE).

#### Dicionário de Dados (Descrição das Colunas)

Abaixo estão descritas as principais colunas extraídas durante as rotinas de coleta de dados (multiplex e relação público/sala):

- **Nome da coluna:** `PUBLICO`  
  - **Descrição da coluna:** Público das sessões.  
  - **Exemplo:** `0`

- **Nome da coluna:** `PAIS_OBRA`  
  - **Descrição da coluna:** País de origem das obras exibidas.  
  - **Exemplo:** `ESTADOS UNIDOS`

---

### Tabelas FSA

Planilha pronta vinda do site da ANCINE.

#### Dicionário de Dados (Descrição das colunas)

- **Nome da coluna:** `Ano`  
  - **Descrição da coluna:** Ano de referência do registro histórico dos dados.  
  - **Exemplo:** `2020`

- **Nome da coluna:** `Execução financeira`  
  - **Descrição da coluna:** Registros dos valores efetivamente pagos pelo FSA em projetos e programas ao longo do tempo.  
  - **Exemplo:** `266,000,000`

---

### pmi_ancine

Por meio de relatórios de transparência obtidos pelo site da ANCINE, foram feitos scrap das informações do pdf usando bibliotecas de python como pdf plumber e pandas.

#### Dicionário de Dados (Descrição das colunas)

- **Nome da coluna:** `Ano`  
  - **Descrição da coluna:** Ano de referência do registro histórico dos dados.  
  - **Exemplo:** `2020`

- **Nome da coluna:** `PMI`  
  - **Descrição da coluna:** Preço médio do ingresso no ano referente, valor de inflação atualizado.  
  - **Exemplo:** `21,1`

---

### quantidade_ano

A coleta de dados foi realizada de forma automatizada através da técnica de *web scraping*, extraindo informações do portal cinemateca. Utilizando a linguagem Python, scripts foram desenvolvidos com o auxílio das bibliotecas **Selenium** (para automação e navegação web) e **Pandas** (para estruturação em DataFrames), as informações foram combinadas com csvs públicos pegos do site oficial da ANCINE.

#### Dicionário de Dados (Descrição das colunas)

- **Nome da coluna:** `data`  
  - **Descrição da coluna:** Ano de referência do registro histórico dos dados.  
  - **Exemplo:** `2020`

- **Nome da coluna:** `Quantidade`  
  - **Descrição da coluna:** A soma total dos filmes brasileiros lançados ano a ano desde 1913.  
  - **Exemplo:** `3208` *(Valor numérico discreto referente ao total de filmes lançados naquele ano)*

---

## Acesso aos Dados

Os arquivos CSV e/ou tabelas geradas nesta fase da coleta estão armazenados e disponíveis para acesso no link abaixo:

**https://drive.google.com/drive/folders/1qgTINXwWEMEoANYlI6FUCQjA4Yu7jQpP**
