from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def investing(link):
    try:
        # Configuração das opções do Chrome para o modo oculto
        options = Options()
        options.add_argument("--headless")  # Ativa o modo oculto

        # Configurando o driver do Chrome
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=options)

        # Abrindo a página do link fornecido
        driver.get(link)

        time.sleep(1)

        # Encontrando todos os elementos <p> dentro da div com id "article"
        content_elements = driver.find_elements(
            "xpath", "//*[@id='article']/div/p")

        # Inicializando uma string para armazenar o texto da notícia
        content_text = ""

        # Iterando sobre os elementos <p> para extrair o texto de cada um
        for element in content_elements:
            content_text += element.text + "\n"  # Adicionando o texto de cada elemento

        return content_text

    except Exception as e:
        print("Erro ao copiar notícia:", e)

    finally:
        # Fechando o navegador
        driver.quit()


def infomoney(link):
    try:
        # Configuração das opções do Chrome para o modo oculto
        options = Options()
        options.add_argument("--headless")  # Ativa o modo oculto

        # Configurando o driver do Chrome
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=options)

        # Abrindo a página do link fornecido
        driver.get(link)

        time.sleep(1)

        # Encontrando todos os elementos <p> dentro da div com id "article"
        content_elements = driver.find_elements(
            "xpath", "/html/body/main/article/p")

        # Inicializando uma string para armazenar o texto da notícia
        content_text = ""

        # Iterando sobre os elementos <p> para extrair o texto de cada um
        for element in content_elements:
            content_text += element.text + "\n"  # Adicionando o texto de cada elemento

        return content_text

    except Exception as e:
        print("Erro ao copiar notícia:", e)

    finally:
        # Fechando o navegador
        driver.quit()


if __name__ == "__main__":
    text = infomoney(
        "https://www.infomoney.com.br/mundo/javier-milei-e-camara-da-argentina-tem-revanche-hoje-sobre-megapacote/")

    print(text)
