# Projeto: Introdução à Ciência de Dados

**Integrantes:** Ricardo Morais Pistori, João Rafael Gadelha de Araújo, Victor Hugo Araújo de Vasconcelos, Kaio Vitor Santos de Lima

**Tema:** Uma breve análise sobre o desenvolvimento do mercado cinematográfico no Brasil (1997 - 2025).

---

## Sobre o Conjunto de Dados
O conjunto de dados mapeia a evolução histórica do mercado cinematográfico brasileiro. Ele abrange dados históricos, incluindo o total de salas disponíveis por ano e a relação de público médio por sala desde a década de 1970 até os anos recentes. Esses dados permitem analisar o ritmo de expansão do setor, o impacto da transição para os complexos multiplex e as flutuações de demanda do público ao longo das décadas.

## Processo de Coleta de Dados
A coleta de dados foi realizada de forma automatizada através da técnica de *web scraping*, extraindo informações do portal especializado *Filme B*. Utilizando a linguagem Python, scripts foram desenvolvidos com o auxílio das bibliotecas **Selenium** (para automação e navegação web) e **Pandas** (para estruturação em DataFrames). 

O algoritmo localiza as tabelas HTML corretas usando filtros de texto e tamanho, extrai o código bruto e o converte para um formato tabular estruturado, salvando os resultados para análise.

## Dicionário de Dados (Descrição das Colunas)

Abaixo estão descritas as principais colunas extraídas durante as rotinas de coleta de dados (multiplex e relação público/sala):

* **Nome da coluna:** `Ano`
    * **Descrição da coluna:** Ano de referência do registro histórico dos dados.
    * **Exemplo:** `2020`

* **Nome da coluna:** `Total_Salas`
    * **Descrição da coluna:** O número total acumulado de salas multiplex em operação no Brasil durante o ano avaliado.
    * **Exemplo:** `2757`

* **Nome da coluna:** `Média por Sala`
    * **Descrição da coluna:** A média anual de espectadores (público) que frequentou cada sala de cinema no período especificado.
    * **Exemplo:** `25000` *(Valor numérico contínuo referente à lotação média)*

---

## Acesso aos Dados

Os arquivos CSV e/ou tabelas geradas nesta fase da coleta estão armazenados e disponíveis para acesso no link abaixo:

**https://drive.google.com/drive/folders/1qgTINXwWEMEoANYlI6FUCQjA4Yu7jQpP**
