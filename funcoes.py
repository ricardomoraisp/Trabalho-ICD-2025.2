from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from io import StringIO
import pandas as pd
from selenium.webdriver.common.by import By

def coleta_dados_multiplex(driver: webdriver, texto_busca: str, ano: int) -> pd.DataFrame:

    """
    Gerencia a coleta de dados mapeando automaticamente o código do ranking de acordo com o ano informado.

    Fluxo:
        1. Verifica o 'ano' passado como parâmetro através de condicionais (if/elif/else).
        2. Atribui o 'codigo_ranking' adequado correspondente àquele período histórico.
        3. Executa a função 'coleta_tabelas' passando os parâmetros estabelecidos e um tamanho de tabela fixo em "460".
        4. Retorna o DataFrame resultante da coleta.
        5. Em caso de falha, captura a exceção, imprime o erro no console e retorna None.

    Args:
        driver: Instância do WebDriver utilizada para a navegação.
        texto_busca: Texto que deve estar presente dentro da tabela para ajudar a localizá-la.
        ano: Inteiro representando o ano da pesquisa, usado para deduzir o código do ranking.

    Returns:
        pd.DataFrame: Um DataFrame contendo os dados estruturados da tabela, se a coleta for bem-sucedida.
        None: Caso ocorra alguma exceção (ex: tabela não carregou a tempo).
    """
    try:
        if ano >= 2016:
            codigo_ranking = "R06"
        elif 2013 <= ano <= 2015:
            codigo_ranking = "R07"
        elif 2010 <= ano <= 2012:
            codigo_ranking = "R08"
        elif ano == 2009:
            codigo_ranking = "R09"
        elif ano == 2008:
            codigo_ranking = "R08"
        elif ano == 2007:
            codigo_ranking = "R07"
        elif 2003 <= ano <= 2006:
            codigo_ranking = "R05"
        else:
            codigo_ranking = "R05"

        # Mude a linha final para esta ordem:
        return coleta_tabelas(driver, texto_busca, str(ano), codigo_ranking, "460")

    except Exception as e:
        print(f"\n ERRO: Tabela de {ano} não carregou a tempo ou não foi encontrada. Detalhes: {e}")
        return None
    

def coleta_tabelas(driver: webdriver, texto_busca: str, ano: str, codigo_rank: str, tamanho: str) -> pd.DataFrame:
        
    """
    Extrai uma tabela específica de uma página da web e a converte em um DataFrame do Pandas.

    Fluxo:
        1. Constrói a URL de busca dinâmica utilizando o ano e o código do ranking.
        2. Acessa a página da web gerada.
        3. Define um XPath buscando uma tabela que tenha uma largura (width) específica e contenha um determinado texto.
        4. Aguarda até 10 segundos para que a tabela alvo carregue na tela.
        5. Extrai o código HTML bruto da tabela.
        6. Lê o HTML usando o Pandas e retorna o primeiro DataFrame encontrado.

    Args:
        driver: Instância do WebDriver utilizada para a navegação.
        texto_busca: Texto que deve estar presente dentro da tabela para ajudar a localizá-la no HTML.
        ano: String representando o ano desejado na busca da URL.
        codigo_rank: String representando o código do ranking desejado na busca da URL.
        tamanho: String representando o atributo 'width' da tabela HTML (ex: "960").

    Returns:
        pd.DataFrame: Um DataFrame contendo os dados estruturados da tabela encontrada.

    Raises:
        TimeoutException: (Implícito pelo WebDriverWait) Se a tabela não for encontrada na página dentro de 10 segundos.
    """
        
    url = f"https://www.filmeb.com.br/database2/html/Seleciona_Modelo.php?st_indica_processo=PESQUISA&get_tipo_ranking={codigo_rank}&get_ano={ano}"
        
    driver.get(url)

    xpath = f"//table[@width='{tamanho}' and contains(., '{texto_busca}')]"
    
    # Espera máxima de até 10 segundos para o carregamento da página
    tabela_alvo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    
    html_tabela = tabela_alvo.get_attribute('outerHTML')

    df = pd.read_html(StringIO(html_tabela))[0]
    
    return df