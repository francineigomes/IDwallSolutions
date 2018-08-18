# IDwallSolutions

**Obs.**:
- Este projeto foi desenvolvido em um computador com sistema operacional Windows. 
- Instalou-se o conjunto de pacotes Anaconda.
- Utilizou-se a interface de desenvolvimento spyder.

# Desafio 1: Manipulação de string

A solução do desafio 1 está implementada no módulo wrapJustify.py.
Para verificar o resultado basta seguir os passos listados abaixo.
- Baixar a pasta codes.
- Abrir o terminal na pasta codes. E executar os comandos abaixo
- python
- import wrapJustify as wJ
- saida = wJ.text_wrapper_justified(text,line_width)

Onde
- text: corresponde ao texto a ser processado
- line_width: corresponde ao número de caracteres permitidos por linha

A variável "saida" será uma tupla contendo os resultados solicitados pelo desafio 1.
print(saida[0]) : imprime o texto com limite de número de caracteres por linha
print(saida[1]) : imprime o texto com limite de número de caracteres por linha e com o texto justificado

# Desafio 2: Crawlers

## Parte 1
Na parte 1 foi solicitado listar as threads que estão bombando no Reddit no momento!. São consideradas como bombando as threads com 5000 ou mais pontos.

**Obs.**:
- Para este desafio foi necessário a instalação da API [praw](https://praw.readthedocs.io/en/latest/)
- Para instalar o praw basta executar o comando (conda install -c conda-forge praw) no prompt do anaconda 
- Foi necessário criar um [app](https://www.reddit.com/prefs/apps) no reddit

A solução do parte 1 do desafio 2 está implementada no módulo scrapReddit.py.
Para verificar o resultado basta seguir os passos listados abaixo.
