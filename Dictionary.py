from bs4 import BeautifulSoup 
import requests

print('-='*15)
print('Dicionario Ingles para Portugues')
print('-='*15)

palavra = input('Digite a palavra: ').lower()

HTML = requests.get(f"https://www.infopedia.pt/dicionarios/ingles-portugues/{palavra}")#requests abre o link e passa para HTML
soup = BeautifulSoup(HTML.text, 'html.parser')#com o link pega as tags hmtl com informacoes
text = soup.find("span", attrs={'class':'dolTraduzTrad'}).text #soup procura a tag que estamos pedindo com a class e .text pega tira as tags html

print(f'\nSignificado de {palavra}:')
print(text)