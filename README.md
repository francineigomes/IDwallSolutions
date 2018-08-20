# IDwallSolutions

**Obs.**:
- Este projeto foi desenvolvido em um computador com sistema operacional Windows. 
- Instalou-se o conjunto de pacotes Anaconda.
- Utilizou-se a interface de desenvolvimento spyder.

# Desafio 1: Manipulação de string

A solução do desafio 1 está implementada no módulo wrapJustify.py.
Para verificar o resultado basta seguir os passos listados abaixo:
- Realizar o download da pasta codes.
- Abrir o terminal na pasta codes e executar os comandos
- ipython
- import wrapJustify as wJ
- saida = wJ.text_wrapper_justified(text,line_width)

Onde
- text: corresponde ao texto a ser processado
- line_width: corresponde ao número de caracteres permitidos por linha

A variável "saida" será uma tupla contendo os resultados solicitados pelo desafio 1.
O comando print(saida[0]) imprime o texto com limite de número de caracteres por linha
O comando print(saida[1]) imprime o texto com limite de número de caracteres por linha e com o texto justificado

# Desafio 2: Crawlers

## Parte 1
Na parte 1 foi solicitado listar as threads que estão bombando no Reddit no momento!. São consideradas como bombando as threads com 5000 ou mais pontos.

**Obs.**:
- Para este desafio foi necessário a instalação da API [praw](https://praw.readthedocs.io/en/latest/)
- Para instalar o praw basta executar o comando (conda install -c conda-forge praw) no prompt do anaconda 
- Foi necessário criar um [app](https://www.reddit.com/prefs/apps) no reddit

A solução da parte 1 do desafio 2 está implementada no módulo scrapReddit.py.
Para verificar o resultado basta seguir os passos listados abaixo:
- Faça o download da pasta codes.
- Abra o terminal na pasta codes e execute os comandos abaixo
- ipython
- import scrapReddit as sReddit
- get_document = sReddit.reddit_list(subreddit_name, min_ups, max_limit)

Onde
- subreddit_name: corresponde ao Subreddit a pesquisado
- get_document: corresponde à lista de threads bombando no momento no subreddit_name
- min_ups: correspondo ao mínimo de pontos para a thread se considerada "bombando"
- max_limit: corresponde à profundidade da busca, pois na API "praw" é necessário informar quantas threads serão retornadas a cada busca

**Obs.**:
- Optou-se por essa forma de implementação para facilitar o uso da função "reddit_list" na solução do Desafio 2 - Parte 2.

O comando print(get_document) imprime a lista de threads bombando para o Subreddit pesquisado.

## Parte 2
Na parte 2 foi solicitado criar um robô que ao receber uma lista de subreddits retorna a lista de threads que estão bombando em cada subreddits. Lembrando que uma thread é considerada bombando se possuir 5000  ou mais pontos.

**Obs.**:
- Para este desafio foi necessário criar uma conta no Telegram.
- Depois de criada a conta é possível criar um bot. Para isso é preciso: 1) logar na conta, 2) Procurar pelo usuário "BotFather". Ele é um bot que ajuda criar outros bots. Então basta escolher a opção de criar novo bot e seguir os passos indicados. Ao final será gerado um TOKEN. Esse TOKEN é utilizado no script "bot.py" pois ele serve com uma autorização para controlar o bot criado.
- O nome do bot criado para esse desafio é: "IDwallChallenge"
- O script "bot.py" controla o bot. Dentro desse script é feito a chamada a função "reddit_list" implementada dentro do módulo desenvolvido para a solução da PARTE 1. Lembrando que esta função retorna uma lista de threads para o subreddit informado.
- Foi necessário instalar o pacote [telepot](https://telepot.readthedocs.io/en/latest/). Para a sua instalação basta digitar: pip install telepot.

A solução da parte 2 do desafio 2 está implementada no módulo bot.py.
Para verificar o resultado basta seguir os passos listados abaixo:
- Vá ao Telegram e procure pelo bot "IDwallChallenge"
- Envie para o bot a lista de threads desejada, seguindo o formado indicado pelo desefio. Isso é necessário pois a implementação atual ainda não trata strings fora do padrão sugerido pelo desafio.
- Faça o download da pasta codes.
- Abra o terminal na pasta codes e execute o comando abaixo
- ipython bot.py


**Obs.**:
- O bot só responde se já tiver recebido a mensagem !!!
- Conforme explicado anteriormente, a variável "max_limit" corresponde ao máximo de threads buscadas, para que desse conjunto sejam verificadam as que possuem 5000 ou mais pontos. O valor default escolhido foi "max_limit=100".







