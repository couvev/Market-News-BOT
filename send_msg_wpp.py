from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def send(msg, titulo):
    # Inicializa o driver do Chrome
    options = webdriver.ChromeOptions()
    options.add_argument(
        r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default")
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=options)

    # Abre uma página da web
    driver.get("https://web.whatsapp.com/")

    # Espera para garantir que a página seja carregada completamente
    time.sleep(22)

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

    time.sleep(2)

    enviar = driver.find_element(
        "xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')

    enviar.click()

    time.sleep(4)

    # Fecha o navegador
    driver.quit()


if __name__ == "__main__":
    # Esta parte do código será executada somente quando o script for executado diretamente
    message = "O mercado acionário dos EUA iniciou o dia com um avanço significativo, impulsionado principalmente pelos excelentes resultados trimestrais da Alphabet, que ultrapassou a marca de 2 trilhões de dólares em valor de mercado. Além disso, a estabilidade na leitura da inflação, que veio conforme o esperado, contribuiu para acalmar as preocupações relacionadas às altas taxas de juros. Os índices de referência, incluindo o Dow Jones, S&P 500 e Nasdaq Composite, registraram ganhos logo na abertura, refletindo um otimismo cauteloso entre os investidores.\n\nSaiba mais: https://br.investing.com/news/economy/wall-st-abre-em-alta-alphabet-supera-us2-tri-em-valor-de-mercado-1237725"
    titulo = "Wall St abre em alta; Alphabet supera US$2 tri em valor de mercado"
    send(message, titulo)
