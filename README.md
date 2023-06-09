# Documentação Anime Quest
Este repositório contém um conjunto de ferramentas que podem ser úteis para programadores que trabalham em projetos relacionados ao mundo dos animes e mangás.


## aq_leitor_de_barras.py
O script **aq_leitor_de_barras.py** é uma ferramenta que pode ser utilizada para automatizar a busca de informações de figuras de animes e mangás. Ele é capaz de localizar a página correspondente de um item no site [MyFigureCollection](https://myfigurecollection.net/) utilizando um GTIN (Global Trade Item Number) como input.

### Utilização
Para utilizar o script, basta executá-lo a partir do terminal, informando o GTIN como argumento:
```py
python aq_leitor_de_barras.py <GTIN>
```
O script irá abrir em seu navegador padrão a URL da página correspondente no site [MyFigureCollection](https://myfigurecollection.net/).
#### Dependências
O código utiliza as seguintes bibliotecas do Python:
- **webbrowser**: Biblioteca padrão do Python que fornece uma interface simples para abrir URLs em um navegador da web padrão do sistema.
- **selenium**: Uma biblioteca de automação de navegador que permite simular interações do usuário com páginas da web.
- **webdriver**: Um submódulo do selenium que fornece uma API para controlar diferentes navegadores da web de forma programática.
- **chrome.service**: Um submódulo do selenium.webdriver que fornece a classe Service, usada para configurar o executável do ChromeDriver.
- **chrome.options**: Um submódulo do selenium.webdriver que fornece a classe Options, usada para configurar as opções do ChromeDriver.

Certifique-se de ter todas essas bibliotecas instaladas antes de executar o código acima. Para instalar as bibliotecas selenium e webdriver, você pode utilizar o gerenciador de pacotes pip:
```py
pip install selenium webdriver
```


## aq_extract_data_to_csv.py
Este é um script em Python que extrai dados de uma figura/item do site MyFigureCollection e salva em um arquivo CSV. Ele utiliza a biblioteca requests para fazer requisições HTTP, a biblioteca BeautifulSoup para fazer a análise e parse do HTML e a biblioteca Pandas para criar um dataframe e salvar em formato CSV.

### Utilização
Para extrair os dados de uma figura/item do MyFigureCollection, basta chamar a função **extract_data_to_csv** e passar a URL da página como argumento:
```py
extract_data_to_csv('https://myfigurecollection.net/item/906740')
```

#### Dependências
As seguintes bibliotecas são utilizadas no script e precisam estar instaladas:
- requests
- BeautifulSoup
- pandas
- unidecode

Você pode instalá-las através do comando pip:
```py
pip install requests beautifulsoup4 pandas unidecode
```
#### Limitações
O script foi testado apenas com um tipo de página do MyFigureCollection e pode não funcionar corretamente com outras páginas do site. É importante lembrar que o site pode mudar a estrutura do HTML a qualquer momento, o que pode quebrar o script. Caso tenha problemas com alguma página em específico, sinta-se livre para reportar um issue.




