import requests
from bs4 import BeautifulSoup
import pandas as pd
from unidecode import unidecode

def extract_data_to_csv(url):
    # faz a requisição HTTP
    response = requests.get(url)

    # cria o objeto BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # obtém o título da página
    title = soup.select_one('.headline')['title']

    # extrai os dados
    data = []
    for field in soup.select('.form-field'):
        label = field.select_one('.form-label').text.strip()
        value = unidecode(field.select_one('.form-input').text.replace('\xa0', ' ').strip())

        if label == 'Releases':
            # divide o campo Releases em três campos separados
            idx1 = value.index('Y=')
            idx2 = value.index('*')
            releases = value[:idx1].strip()
            y = value[idx1+2:idx2].strip()
            barcode = value[idx2+1:].strip()
            data.append(['Releases', releases])
            data.append(['Yene', y])
            data.append(['Barcode', barcode])
        else:
            data.append([label, value])
    
    data.append(['URL', url])

    # cria um dataframe do pandas e salva em um arquivo CSV
    df = pd.DataFrame(data, columns=['Campo', 'Valor'])
    filename = title[:25] + '.csv'
    filename = filename.replace('/', ' ')
    df.to_csv(filename, index=False, sep=';', encoding='utf-8')


extract_data_to_csv('https://myfigurecollection.net/item/906740')
