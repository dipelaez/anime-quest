# Documentação Anime Quest
Este repositório contém um conjunto de ferramentas que podem ser úteis para programadores que trabalham em projetos relacionados ao mundo dos animes e mangás.


## aq_leitor_de_barras.py
O script **aq_leitor_de_barras.py** é uma ferramenta que pode ser utilizada para automatizar a busca de informações de figuras de animes e mangás. Ele é capaz de extrair informações a partir de um GTIN (Global Trade Item Number) e utilizar esses dados para localizar a página correspondente no site [MyFigureCollection](https://myfigurecollection.net/).

### Utilização
Para utilizar o script, basta executá-lo a partir do terminal, informando o GTIN como argumento:
```py
python aq_leitor_de_barras.py <GTIN>
```
O script irá abrir em seu navegador padrão a URL da página correspondente no site [MyFigureCollection](https://myfigurecollection.net/).
#### Dependências
O script foi escrito em Python 3 e depende das bibliotecas requests e beautifulsoup4. Você pode instalá-las utilizando o gerenciador de pacotes pip:
```py
pip install requests beautifulsoup4
```


