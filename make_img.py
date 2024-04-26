from PIL import Image, ImageDraw, ImageFont

# Abre a imagem
image = Image.open('imagem.jpg')

# Cria um objeto ImageDraw
draw = ImageDraw.Draw(image)

# Especifica a fonte e o tamanho do texto
# Substitua 'arial.ttf' pelo caminho da sua fonte
font = ImageFont.truetype('arial.ttf', 30)

# Especifica a posição e o texto a ser adicionado
position = (50, 50)  # Posição do canto superior esquerdo do texto
text = "Texto que você deseja adicionar"

# Adiciona o texto à imagem
draw.text(position, text, fill="white", font=font)

# Salva a imagem com o texto adicionado
image.save('imagem_com_texto.jpg')
