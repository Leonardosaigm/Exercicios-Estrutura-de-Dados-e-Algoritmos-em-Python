# #Olá,
# Para revisar o conteúdo prático sobre expressões regulares, implemente o exercício abaixo. Logo em seguida você
# acessar a aula em vídeo com a solução
# Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
# - Números
# - CEPs
# - URLs

import re

texto = "Minha casa fica na rua Carneiro, 78. O Cep é 88388-000 e meu site é https://www.iaexpert.academy " \
        "http://iaexpert.com.br "
print(re.findall('\d', texto))
print(re.findall('\d{5}-\d{3}', texto))
print(re.findall('https?:\W{2}www.\w+.\w+', texto))
print(re.findall('https?://[A-Za-z0-9./]+', texto))
# Professor re.findall('https?://[A-Za-z0-9./]+', texto)
