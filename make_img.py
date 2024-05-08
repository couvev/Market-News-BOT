from PIL import Image, ImageDraw, ImageFont
import grab_mkt_info as gmi
import datetime as dt


def new():
    # Abre a imagem
    image = Image.open('base.jpg')

    # Cria um objeto ImageDraw
    draw = ImageDraw.Draw(image)

    # Especifica a fonte e o tamanho do texto
    font_path_bold = 'OpenSans-Bold.ttf'
    font = ImageFont.truetype(font_path_bold, 48)

    # DATA
    # Obtendo a data atual
    data_atual = dt.datetime.today()
    # Formatando para o formato desejado
    data_formatada = data_atual.strftime("%d/%m/%Y")
    # Especifica a posição e o texto a ser adicionado
    position = (110, 155)
    text = data_formatada
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)

    font = ImageFont.truetype('OpenSans-Bold.ttf', 43)

    infos = gmi.ibov()

    # IBOVESPA
    position = (485, 402)
    text = infos['pontos'][:-3]
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['ibov_vari'] and "-" not in infos['ibov_vari']:
        position = (770, 395)
        text = f"+{infos['ibov_vari']}%"
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 395)
        text = f"{infos['ibov_vari']}%"
        draw.text(position, text, fill="red", font=font)

    # MAIOR ALTA
    position = (485, 543)
    text = infos['alta'][:-3]
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['alta_vari'] and "-" not in infos['alta_vari']:
        position = (770, 543)
        text = infos['alta_vari']
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 543)
        text = infos['alta_vari']
        draw.text(position, text, fill="red", font=font)

    # MAIOR BAIXA
    position = (485, 685)
    text = infos['baixa'][:-3]
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['baixa_vari'] and "-" not in infos['baixa_vari']:
        position = (770, 685)
        text = infos['baixa_vari']
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 685)
        text = infos['baixa_vari']
        draw.text(position, text, fill="red", font=font)

    # DOWN JONES
    position = (485, 825)
    text = infos['dw']
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['dw_vari'] and "-" not in infos['dw_vari']:
        position = (770, 825)
        text = infos['dw_vari']
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 825)
        text = infos['dw_vari']
        draw.text(position, text, fill="red", font=font)

    # S&P 500
    position = (485, 968)
    text = infos['sp']
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['sp_vari'] and "-" not in infos['sp_vari']:
        position = (770, 968)
        text = infos['sp_vari']
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 968)
        text = infos['sp_vari']
        draw.text(position, text, fill="red", font=font)

    # IFIX
    position = (485, 1111)
    text = infos['ifix']
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['ifix_vari'] and "-" not in infos['ifix_vari']:
        position = (770, 1111)
        text = infos['ifix_vari']
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 1111)
        text = infos['ifix_vari']
        draw.text(position, text, fill="red", font=font)

    # DOLAR
    position = (485, 1253)
    text = f"R${infos['dolar'][:-2]}"
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['dolar_vari'] and "-" not in infos['dolar_vari']:
        position = (770, 1253)
        text = infos['dolar_vari']
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 1253)
        text = infos['dolar_vari']
        draw.text(position, text, fill="red", font=font)

    # BITCOIN
    position = (420, 1395)
    text = infos['bit']
    # Adiciona o texto à imagem
    draw.text(position, text, fill="white", font=font)
    if "−" not in infos['bit_vari'] and "-" not in infos['bit_vari']:
        position = (770, 1395)
        text = f"+{infos['bit_vari']}"
        draw.text(position, text, fill="green", font=font)
    else:
        position = (770, 1395)
        text = infos['bit_vari']
        draw.text(position, text, fill="red", font=font)

    # Salva a imagem com o texto adicionado
    image.save('new.jpg')
