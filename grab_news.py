import feedparser
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import make_copy as mc
import send_msg_tel as smt
import send_msg_wpp as smw
import asyncio


def copiar_noticia(link):
    try:
        # Configurando o driver do Chrome
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)

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


# URL do feed RSS
url_feed = "https://br.investing.com/rss/news_14.rss"

# Inicialmente, a última notícia é uma string vazia
ultima_noticia = ""


while True:

    try:
        # Fazendo a requisição e lendo o feed
        feed = feedparser.parse(url_feed)

        # Verificando se a requisição foi bem-sucedida
        if feed.status == 200:
            print("Feed lido com sucesso!")
            # Extraindo e imprimindo informações do feed
            if len(feed.entries) > 0:
                entry = feed.entries[0]  # A primeira entrada é a mais recente
                if entry.link != ultima_noticia:
                    print("Nova notícia encontrada:")
                    print("Título:", entry.title)
                    print("Link:", entry.link)
                    print("Publicado em:", entry.published)
                    print("-" * 50)
                    # Atualiza o link da última notícia
                    ultima_noticia = entry.link

                    text = copiar_noticia(ultima_noticia)

                    formated_text = mc.create(text)

                    formated_text = formated_text + f"\n\nSaiba mais: {
                        ultima_noticia}"

                    # Enviar para WhatsApp
                    smw.send(formated_text, entry.title)

                    formated_text = f"{entry.title}\n\n" + formated_text

                    # Enviar para Telegram
                    asyncio.run(
                        smt.send(formated_text, entry.enclosures[0].href))

                    print(formated_text)

                else:
                    print("Nenhuma nova notícia encontrada.")
            else:
                print("Feed vazio.")
    except Exception as e:
        print("Erro ao ler o feed:", feed.status, e)
        time.sleep(60)

    # Aguarda um tempo antes de verificar novamente o feed
    time.sleep(60)
