# 📊 Bot de Fechamento de Mercado e Notícias Financeiras

Bem-vindo ao repositório **Bot de Fechamento de Mercado e Notícias Financeiras**! 🤖 Este projeto automatiza a coleta diária de informações de mercado, cria uma imagem resumindo os principais índices financeiros, e distribui tanto a imagem quanto resumos de notícias financeiras via Telegram e WhatsApp. Além disso, o bot pode ser configurado para enviar resumos de notícias financeiras de fontes selecionadas, processadas pela API do ChatGPT.

---

## ✨ Funcionalidades

- **Coleta Automatizada de Dados de Mercado**: Obtém as últimas informações sobre IBOVESPA, DOW JONES, S&P 500, IFIX, Dólar, Bitcoin, entre outros índices.
- **Geração Dinâmica de Imagens**: Cria uma imagem diária com o resumo do mercado utilizando as informações coletadas.
- **Envio Automatizado de Mensagens**: Envia automaticamente a imagem gerada e resumos de notícias financeiras para grupos no Telegram e WhatsApp.
- **Resumos de Notícias Financeiras**: Coleta notícias de sites selecionados, gera um resumo usando a API do ChatGPT, e envia para os grupos configurados.
- **Execução Programada**: O bot roda automaticamente em horários específicos para garantir que você receba sempre as últimas atualizações.

---

## 🚀 Configuração e Instalação

1. **Clone o Repositório**:
   \`\`\`bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   \`\`\`

2. **Instale as Dependências**:
   Certifique-se de ter o Python 3.8+ instalado. Depois, instale os pacotes necessários:
   \`\`\`bash
   pip install -r lib.txt
   \`\`\`

3. **Configure as Variáveis de Ambiente**:
   Crie um arquivo \`.env\` no diretório raiz e adicione suas chaves de API e outras credenciais:
   \`\`\`bash
   TEL_BOT_KEY=sua-chave-do-bot-telegram
   OPENAI_API_KEY=sua-chave-api-openai
   \`\`\`

4. **Execute o Bot**:
   Para testar o sistema e gerar uma imagem manualmente, você pode executar:
   \`\`\`bash
   python main.py
   \`\`\`

---

## 🌲 Estrutura de Pastas

\`\`\`bash
├── main.py # Script principal que roda todo o processo
├── make_img.py # Script para gerar a imagem de fechamento do mercado
├── send_mkt_info.py # Script que organiza e programa a execução
├── send_msg_tel.py # Script para enviar mensagens para o Telegram
├── send_msg_wpp.py # Script para enviar mensagens para o WhatsApp
├── grab_mkt_info.py # Script para coletar informações de mercado
├── grab_news.py # Script para coletar e resumir notícias financeiras
├── base.jpg # Imagem base usada para o resumo do mercado
├── lib.txt # Lista de dependências do projeto
└── .env # Variáveis de ambiente (não incluído no repositório)
\`\`\`

---

## 🔧 Exemplos de Código

Aqui estão alguns trechos de código para ilustrar como o bot funciona:

### Coleta de Informações de Mercado

O script \`grab_mkt_info.py\` faz a coleta de dados dos principais índices financeiros:

\`\`\`python
def ibov():
result = {}
try: # Configuração das opções do Chrome para o modo oculto
options = Options()
options.add_argument("--headless") # Ativa o modo oculto

        # Configurando o driver do Chrome
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=options)

        # Coletando dados do IBOVESPA
        driver.get("https://economia.uol.com.br/cotacoes/bolsas/")
        time.sleep(4)

        pontos = driver.find_element(By.XPATH, "xpath")
        result['pontos'] = pontos.text

        # Coleta de outros índices...
    except Exception as e:
        print("Erro ao copiar:", e)
    finally:
        driver.quit()
        return result

\`\`\`

### Geração da Imagem

O script \`make_img.py\` cria uma imagem com as informações de mercado:

\`\`\`python
def new():
image = Image.open('base.jpg')
draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('OpenSans-Bold.ttf', 43)
    infos = gmi.ibov()

    # Adiciona informações do IBOVESPA na imagem
    position = (485, 402)
    text = infos['pontos'][:-3]
    draw.text(position, text, fill="white", font=font)

    # Adiciona informações dos outros índices...
    image.save('new.jpg')

\`\`\`

### Envio das Mensagens

O script \`send_msg_tel.py\` cuida do envio das imagens para o Telegram:

\`\`\`python
async def send_photo():
bot = Bot(os.environ.get("TEL_BOT_KEY"))
chat_id = '-1002005750638'
photo_path = 'new.jpg'
caption = "Fechamento do mercado"
await bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'), caption=caption)
\`\`\`

E o script \`send_msg_wpp.py\` cuida do envio para o WhatsApp:

\`\`\`python
def send(msg, titulo):
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\thiag\AppData\Local\Google\Chrome\User Data\Default")
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)

    driver.get("https://web.whatsapp.com/")
    time.sleep(30)
    campo_de_entrada = driver.find_element(By.XPATH, "xpath")
    campo_de_entrada.send_keys(msg)
    driver.quit()

\`\`\`

### Resumo de Notícias

O script \`grab_news.py\` coleta e resume notícias financeiras:

\`\`\`python
def cnn(link):
try:
options = Options()
options.add_argument("--headless")
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)
driver.get(link)

        content_elements = driver.find_elements(By.XPATH, "xpath")
        content_text = "".join([element.text + "\n" for element in content_elements])
        return content_text
    finally:
        driver.quit()

\`\`\`

Este conteúdo é posteriormente resumido usando a API do OpenAI:

\`\`\`python
def create(text):
chat_completion = client.chat.completions.create(
messages=[
{"role": "system", "content": "Faca um resumo dessa noticia, com no maximo 7 linhas, sem titulo."},
{"role": "user", "content": text}
],
model="gpt-4-turbo-2024-04-09",
)
return chat_completion.choices[0].message.content
\`\`\`

---

## 📅 Execução Programada

O script \`send_mkt_info.py\` organiza a execução automatizada das tarefas:

\`\`\`python
import schedule
import make_img as mk
import send_msg_tel as smt
import send_msg_wpp as smw

def send_daily():
mk.new()
smt.send_photo()
smw.send_photo()

schedule.every().day.at("17:02").do(send_daily)

while True:
schedule.run_pending()
\`\`\`

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver ideias para melhorias ou novas funcionalidades, sinta-se à vontade para fazer um fork deste repositório, implementar suas alterações e submeter um pull request.

---

## 📧 Contato

Para dúvidas ou sugestões, entre em contato através do email **thiagolcsalves@gmail.com**.
