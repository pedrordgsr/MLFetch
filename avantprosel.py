import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from dotenv import load_dotenv
load_dotenv();
import os;

# Carregar a planilha
planilha = pd.read_csv('planilhas/avantpro.csv')

servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_extension('Avantpro.crx')
navegador = webdriver.Chrome(service=servico, options=options)

# Abrir Mercado Livre
navegador.get("https://www.mercadolivre.com.br/")
time.sleep(2)
navegador.find_element(By.CLASS_NAME, "menu-avantpro").click()
navegador.find_element(By.ID,'btnLoginMenu').click()
navegador.find_element(By.ID,'userEmail').send_keys(os.getenv('LOGIN'))
navegador.find_element(By.ID,'btnSubmitLogin').click()
time.sleep(3)

# Criar arquivo CSV para salvar os resultados
with open('planilhas/resultados.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Produto", "Sem Medalha", "Menor Preco", "Maior Preco", "Concorrencia"])

    # Iterar sobre cada produto na planilha
    for index, row in planilha.iterrows():
        produto = row[planilha.columns[0]]
        
        # Pesquisar o produto
        search_box = navegador.find_element(By.ID,'cb1-edit')
        search_box.clear()
        search_box.send_keys(produto)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        
        # Extrair os elementos de preço
        precos_elementos = navegador.find_elements(By.CLASS_NAME, 'metrics-data')
        
        # Verificar o nível de concorrência
        concorrencia = "N/A"  # Valor padrão caso não seja encontrado nenhum botão
        
        try:
            # Encontrar o botão de concorrência e identificar a classe
            botao_concorrencia = navegador.find_element(By.ID, 'analysisBtn')
            if 'btn-error' in botao_concorrencia.get_attribute('class'):
                concorrencia = "Alta"
            elif 'btn-warning' in botao_concorrencia.get_attribute('class'):
                concorrencia = "Media"
            elif 'btn-success' in botao_concorrencia.get_attribute('class'):
                concorrencia = "Baixa"
        except:
            # Se o botão não for encontrado ou ocorrer erro
            concorrencia = "Não encontrado"
        
        # Garantir que temos elementos suficientes antes de acessar
        if len(precos_elementos) > 20:
            semMedalha = precos_elementos[0].text.strip()  # Remove espaços em branco e caracteres extras
            menor_preco = precos_elementos[19].text.strip()
            maior_preco = precos_elementos[20].text.strip()
        else:
            semMedalha = "N/A"
            menor_preco = "N/A"
            maior_preco = "N/A"
        
        # Salvar os resultados no CSV
        writer.writerow([produto, semMedalha, menor_preco, maior_preco, concorrencia])
        
        # Printar para debug
        print(f"Produto: {produto}")
        print(f"Sem Medalha: {semMedalha}")
        print(f"Menor preço: {menor_preco}")
        print(f"Maior preço: {maior_preco}")
        print(f"Concorrência: {concorrencia}")

# Fechar o navegador
navegador.quit()
