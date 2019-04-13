## Como instalar Scrapy no Windows

Para instalar as dependências e a biblioteca Scrapy utilize o gerenciados de pacotes python PIP a instalação é feita através da linha de comando (CMD). 

1. Instalar Twisted utilizando o arquivo whl da versão python instalada, os arquivos de instalação podem ser encontrados no site: https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

2. Instalar Scrapy usando pip -> pip install scrapy

3. Instalar a biblioteca -> pip install pypiwin32

Após a instalação o comando `scrapy` estará disponível como uma ferramenta CLI, possibilitando criar novos projetos e executar spiders/crawlers

## Comandos

Os principais comandos scrapy são para criar novos projetos ou executar spiders de um projeto pronto. Abaixo estão os comandos mais utilizados:

```console
>. scrapy startproject myproject
```

stratproject cria um novo projeto com os principais arquivos do FrameWork Scrapy.

```console
>. scrapy genspider <nome spider> <url inicial>
```

O comando genspider cria um novo spider/crawler na pasta spiders do projeto.

```console
>. scrapy crawl <nome spider>
```

O comando crawl executa um spider.

 
## Referências

Para mais detalhes sobre configurações de projeto use sempre como referência a documentação oficial: https://docs.scrapy.org/en/latest/index.html

