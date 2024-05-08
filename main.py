import feedparser
import make_copy as mc
import send_msg_tel as smt
import send_msg_wpp as smw
import asyncio
import grab_news as gn
import time


# URLs dos feeds RSS
urls_feeds = [
    "https://br.investing.com/rss/news_14.rss",
    "https://www.infomoney.com.br/economia/feed/",
    "https://www.cnnbrasil.com.br/economia/investimentos/feed/"
]

# Inicialmente, a última notícia é uma string vazia
ultima_noticia = {url: "" for url in urls_feeds}


while True:
    try:
        for url_feed in urls_feeds:
            print(url_feed)
            # Fazendo a requisição e lendo o feed
            feed = feedparser.parse(url_feed)

            # Verificando se a requisição foi bem-sucedida
            if feed.status == 200:
                print("Feed lido com sucesso!")
                # Extraindo e imprimindo informações do feed
                if len(feed.entries) > 0:
                    # A primeira entrada é a mais recente
                    entry = feed.entries[0]
                    if entry.link != ultima_noticia[url_feed]:
                        print("Nova notícia encontrada:")
                        print("Título:", entry.title)
                        print("Link:", entry.link)
                        print("Publicado em:", entry.published)
                        print("-" * 50)
                        # Atualiza o link da última notícia
                        ultima_noticia[url_feed] = entry.link

                        print("lINK ADICIONADO")

                        if url_feed == "https://br.investing.com/rss/news_14.rss":
                            text = gn.investing(entry.link)
                        elif url_feed == "https://www.infomoney.com.br/economia/feed/":
                            text = gn.infomoney(entry.link)
                        elif url_feed == "https://www.cnnbrasil.com.br/economia/investimentos/feed/":
                            text = gn.cnn(entry.link)

                        print("TEXTO Copiado")

                        formated_text = mc.create(text)

                        print("TEXTO CRIADO")

                        print(f"\n{entry.title}\n")
                        print(f"\n{entry.link}\n")
                        print(f"\n{formated_text}\n")

                        asyncio.run(
                            smt.send(formated_text, entry.title, entry.link))

                        print("TEXTO TELEGRAM ENVIADO")

                        formated_text = formated_text + f"\n\n*Saiba mais:* {
                            entry.link}"

                        print("TEXTO FORMATARDO")

                        # Enviar para WhatsApp
                        smw.send(formated_text, entry.title)

                        print("TEXTO WPP ENVIADO")

                        print(formated_text)

                    else:
                        print("Nenhuma nova notícia encontrada.")
                else:
                    print("Feed vazio.")
    except Exception as e:
        print("Erro:", e, "Status:", feed.status)
        time.sleep(5)

    # Aguarda um tempo antes de verificar novamente o feed
    time.sleep(5)
