from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options


def send(msg, titulo):
    try:
        # Configuração das opções do Chrome para o modo oculto
        # options = Options()
        # options.add_argument("--headless")  # Ativa o modo oculto

        # Inicializa o driver do Chrome
        options = webdriver.ChromeOptions()
        options.add_argument(
            r"user-data-dir=C:\Users\thiag\AppData\Local\Google\Chrome\User Data\Default")
        # options.add_argument(r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default")
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=options)

        # Abre uma página da web
        driver.get("https://web.whatsapp.com/")

        # Espera para garantir que a página seja carregada completamente
        time.sleep(30)

        # Encontra o elemento de entrada pelo id
        canais = driver.find_element(
            "xpath", '//*[@id="app"]/div/div[2]/header/div/div/div/div/span/div/div[1]/div[4]/div/span')

        canais.click()

        time.sleep(2)

        canal = driver.find_element(
            "xpath", '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]')

        canal.click()

        time.sleep(2)

        campo_de_entrada = driver.find_element(
            "xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

        titulo = "*" + titulo + "*"

        campo_de_entrada.send_keys(titulo)
        time.sleep(1)
        campo_de_entrada.send_keys(Keys.SHIFT + Keys.ENTER)
        campo_de_entrada.send_keys(Keys.SHIFT + Keys.ENTER)

        # Divide a mensagem em parágrafos
        paragraphs = msg.split('\n')

        # Envia cada parágrafo como uma mensagem separada
        for paragraph in paragraphs:
            campo_de_entrada.send_keys(paragraph)
            # Pressiona Shift+Enter para inserir uma quebra de linha sem enviar a mensagem
            campo_de_entrada.send_keys(Keys.SHIFT + Keys.ENTER)
            time.sleep(1)  # Aguarda um segundo entre os parágrafos

        time.sleep(5)

        enviar = driver.find_element(
            "xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')

        enviar.click()

        time.sleep(4)

        # Fecha o navegador
        driver.quit()
    except Exception as e:
        raise e


def send_photo():
    try:
        # Configuração das opções do Chrome para o modo oculto
        # options = Options()
        # options.add_argument("--headless")  # Ativa o modo oculto

        # Inicializa o driver do Chrome
        options = webdriver.ChromeOptions()
        options.add_argument(
            r"user-data-dir=C:\Users\thiag\AppData\Local\Google\Chrome\User Data\Default")
        # options.add_argument(r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default")
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=options)

        # Abre uma página da web
        driver.get("https://web.whatsapp.com/")

        # Espera para garantir que a página seja carregada completamente
        time.sleep(20)

        # Encontra o elemento de entrada pelo id
        canais = driver.find_element(
            "xpath", '//*[@id="app"]/div/div[2]/header/div/div/div/div/span/div/div[1]/div[4]/div/span')

        canais.click()

        time.sleep(2)

        canal = driver.find_element(
            "xpath", '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]')

        canal.click()

        time.sleep(2)

        anexo = driver.find_element(
            "xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')

        anexo.click()

        time.sleep(2)

        photo = driver.find_element(
            "xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/input')

        time.sleep(2)

        photo.send_keys(
            r"C:\Users\thiag\OneDrive\Área de Trabalho\Telegram\new.jpg")
        # photo.send_keys(Keys.RETURN)

        time.sleep(2)

        enviar = driver.find_element(
            "xpath", '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')

        enviar.click()

        time.sleep(4)

        # Fecha o navegador
        driver.quit()
    except Exception as e:
        raise e


if __name__ == "__main__":
    # Esta parte do código será executada somente quando o script for executado diretamente
    send("TESTE", "TESTE")
