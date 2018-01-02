import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def Grab(my_url):
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')
    estrangeiro = page_soup.findAll('input', {'id':'nacional'})
    estran = estrangeiro[0]
    moeda = estran['value']
    return moeda

print('Digite [1] Para Dólar Americano US$ \n'
'Digite [2] Para Dólar Australiano A$ \n'
'Digite [3] Para Dólar Canadense C$ \n'
'Digite [4] Para BitCoin B \n'
'Digite [5] Para Euro \n'
'Digite [6] Para Iene \n'
'Digite [7] Para Libra \n'
'Digite [8] Para Peso Argentino $ \n'
'Digite [9] Para Peso Chileno \n'
'Digite [10] Para Peso Uruguaio \n'
'Digite [11] Para Yuan'
)

escolha = int(input('Que Moeda Deseja? '))

if escolha == 1:
    my_url = 'http://dolarhoje.com/'
    print('1,00 Dólar - vale R$',Grab(my_url))

elif escolha == 2:
    my_url = 'http://dolarhoje.com/dolar-australiano-hoje/'
    print('1,00 Dólar Australiano - vale R$',Grab(my_url))

elif escolha == 3:
    my_url = 'http://dolarhoje.com/dolar-canadense-hoje/'
    print('1,00 Dólar Canadense - vale R$',Grab(my_url))

elif escolha == 4:
    my_url = 'http://dolarhoje.com/bitcoin-hoje/'
    print('1,00 Bitcoin - vale R$',Grab(my_url))

elif escolha == 5:
    my_url = 'http://dolarhoje.com/euro/'
    print('1,00 Euro - vale R$',Grab(my_url))

elif escolha == 6:
    my_url = 'http://dolarhoje.com/iene/'
    print('1,00 Iene - vale R$',Grab(my_url))

elif escolha == 7:
    my_url = 'http://dolarhoje.com/libra-hoje/'
    print('1,00 Libra - vale R$',Grab(my_url))

elif escolha == 8:
    my_url = 'http://dolarhoje.com/peso-argentino/'
    print('1,00 Peso Argentino - vale R$',Grab(my_url))

elif escolha == 9:
    my_url = 'http://dolarhoje.com/peso-chileno/'
    print('1,00 Peso Chileno - vale R$',Grab(my_url))

elif escolha == 10:
    my_url = 'http://dolarhoje.com/peso-uruguaio/'
    print('1,00 Peso Uruguaio - vale R$',Grab(my_url))

elif escolha == 11:
    my_url = 'http://dolarhoje.com/yuan-hoje/'
    print('1,00 Yuan - vale R$',Grab(my_url))
