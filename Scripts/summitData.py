import requests
import pandas as pd
from bs4 import BeautifulSoup

url = input("Digite a URL do SITE: ")
subject = input("Digite o assunto da notícia: ")
newsType = input("Digite V para noticia verdadeira e F para noticia Falsa: ")[0:1]

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

# Seleciona todas as tags de parágrafo e cabeçalho
titulos_pg = soup.find_all(['h1'])
content_pg = soup.find_all(['p'])

headline = ""
content = ""

for tag in titulos_pg:
    headline = tag.get_text()

for tag in content_pg:
    content += tag.get_text()


dataFrame = { 'link': url, 'headline': headline, 
             'content': content, 'subject': subject}


if newsType == 'V' or newsType == 'F':
    df = pd.read_csv('DataBase/noticia{}.csv'.format(newsType), sep=';')
    nova_linha = pd.DataFrame(dataFrame, index=[len(df)])
    df = pd.concat([df, nova_linha])
    df.to_csv('DataBase/noticia{}.csv'.format(newsType),index=False)
else:
    pass
