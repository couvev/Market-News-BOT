from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def ibov():
    result = {}
    try:
        # Configuração das opções do Chrome para o modo oculto
        options = Options()
        options.add_argument("--headless")  # Ativa o modo oculto

        # Configurando o driver do Chrome
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=options)

        # Abrindo a página do link fornecido
        driver.get("https://economia.uol.com.br/cotacoes/bolsas/")

        time.sleep(4)

        # Encontrando todos os elementos <p> dentro da div com id "article"
        pontos = driver.find_element(
            "xpath", "/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/span[2]")
        result['pontos'] = pontos.text

        ibov_vari = driver.find_element(
            "xpath", "/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[5]/div/span[2]/span")
        result['ibov_vari'] = ibov_vari.text

        alta = driver.find_element(
            "xpath", '/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[3]/section[1]/div/div[1]/table/tbody/tr[1]/td[1]/a')
        result['alta'] = alta.text

        alta_vari = driver.find_element(
            "xpath", '/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[3]/section[1]/div/div[1]/table/tbody/tr[1]/td[2]/a')
        result['alta_vari'] = alta_vari.text

        baixa = driver.find_element(
            "xpath", '/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[3]/section[1]/div/div[2]/table/tbody/tr[1]/td[1]/a')
        result['baixa'] = baixa.text

        baixa_vari = driver.find_element(
            "xpath", '/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[3]/section[1]/div/div[2]/table/tbody/tr[1]/td[2]/a')
        result['baixa_vari'] = baixa_vari.text

        driver.get('https://br.tradingview.com/symbols/TVC-DJI/')

        time.sleep(4)

        # Encontrando todos os elementos <p> dentro da div com id "article"
        dw = driver.find_element(By.CLASS_NAME, "js-symbol-last")
        result['dw'] = dw.text

        dw_vari = driver.find_element(By.CLASS_NAME, "js-symbol-change-pt")
        result['dw_vari'] = dw_vari.text

        driver.get('https://br.tradingview.com/symbols/SPX/')

        time.sleep(4)

        sp = driver.find_element(By.CLASS_NAME, "js-symbol-last")
        result['sp'] = sp.text

        sp_vari = driver.find_element(By.CLASS_NAME, "js-symbol-change-pt")
        result['sp_vari'] = sp_vari.text

        driver.get('https://br.tradingview.com/symbols/BMFBOVESPA-IFIX/')

        time.sleep(4)

        ifix = driver.find_element(By.CLASS_NAME, "js-symbol-last")
        result['ifix'] = ifix.text

        ifix_vari = driver.find_element(By.CLASS_NAME, "js-symbol-change-pt")
        result['ifix_vari'] = ifix_vari.text

        driver.get('https://br.tradingview.com/symbols/USDBRL/')

        time.sleep(4)

        dolar = driver.find_element(By.CLASS_NAME, "js-symbol-last")
        result['dolar'] = dolar.text

        dolar_vari = driver.find_element(By.CLASS_NAME, "js-symbol-change-pt")
        result['dolar_vari'] = dolar_vari.text

        driver.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')

        time.sleep(4)

        bit = driver.find_element(By.CLASS_NAME, "eZIItc")
        result['bit'] = bit.text

        driver.get('https://www.google.com/search?q=bitcoin')

        time.sleep(4)

        bit_vari = baixa_vari = driver.find_element(
            "xpath", '//*[@id="crypto-updatable_2"]/div[3]/span/span[2]')
        bit_vari_format = bit_vari.text.replace("(", "").replace(")", "")
        result['bit_vari'] = bit_vari_format

    except Exception as e:
        print("Erro ao copiar:", e)

    finally:
        # Fechando o navegador
        driver.quit()
        return result


if __name__ == "__main__":
    a = ibov()

    print(a["ifix"])
