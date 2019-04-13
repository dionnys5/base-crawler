## Como instalar Scrapy no Windows

Para instalar as depend�ncias e a biblioteca Scrapy utilize o gerenciados de pacotes python PIP a instala��o � feita atrav�s da linha de comando (CMD). 

1. Instalar Twisted utilizando o arquivo whl da vers�o python instalada, os arquivos de instala��o podem ser encontrados no site: https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

2. Instalar Scrapy usando pip -> pip install scrapy

3. Instalar a biblioteca -> pip install pypiwin32

Ap�s a instala��o o comando `scrapy` estar� dispon�vel como uma ferramenta CLI, possibilitando criar novos projetos e executar spiders/crawlers

## Comandos

Os principais comandos scrapy s�o para criar novos projetos ou executar spiders de um projeto pronto. Abaixo est�o os comandos mais utilizados:

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

 
## Refer�ncias

Para mais detalhes sobre configura��es de projeto use sempre como refer�ncia a documenta��o oficial: https://docs.scrapy.org/en/latest/index.html

