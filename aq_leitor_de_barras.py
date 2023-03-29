import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurando o objeto Service com o caminho do executável do ChromeDriver
PATH = "C:\webdrivers\chromedriver.exe"
service = Service(PATH)

while True:
    # Pedindo input
    codigo_de_barras = input("Digite o código de barras: ")
    
    # Verificando se o usuário digitou 'q' para sair do programa
    if codigo_de_barras.lower() == 'q':
        break
    
    # Configurando o ChromeOptions para usar o modo headless
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Instanciando o ChromeDriver com o objeto Service
    driver = webdriver.Chrome(service=service, options=options)

    # Acessando o site
    driver.get("https://myfigurecollection.net/browse/search/")

    # Localizando o campo de busca e preenchendo com o código de barra desejado
    search_bar = driver.find_element(By.NAME, "barcode")
    search_bar.send_keys(codigo_de_barras)

    # Pressionando a tecla "enter" para realizar a busca
    search_bar.send_keys(Keys.RETURN)

    # Salvando a URL em que o navegador está
    url = driver.current_url

    # Fechando o browser
    driver.quit()

    # Abrindo a URL no navegador padrão
    webbrowser.open(url)
