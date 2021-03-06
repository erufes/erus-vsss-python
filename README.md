# VSSS ERUS

Projeto de VSSS (Very Small Sized Soccer) da ERUS, desenvolvido em Python

# Instalação de dependências
## Com Simulador

Para compilar o projeto e utilizar o simulador, é necessário instalar a seguinte lista de pacotes:

`g++ cmake libxmu-dev libxi-dev protobuf-compiler libprotobuf-dev pkg-config libzmq5 libzmq3-dev libboost-all-dev libbullet-dev freeglut3 freeglut3-dev`

Caso o pacote `pkg-config` esteja indisponível, instale o `pkgconf`.

Utilize o gerenciador de pacotes da sua distribuição, como `apt` ou `pacman`, para  instalar os pacotes listados.

Também é necessário instalar o vssscorepy, o vss-sdk, pyzmq, OpenCV, numpy e google.

```
$ sudo -H pip install git+https://github.com/VSS-SDK/VSS-CorePy --upgrade
```

Adicionalmente, é necessário compilar os subprojetos do simulador, o que pode ser feito por meio do script `vss-simulator/instalador.sh`. **Certifique-se de que todas as dependências de pacotes foram instaladas antes de rodar os scripts, ou você TERÁ erros de compilação**!

```
$ sudo ./vss-simulator/instalador.sh
```
## Sem Simulador
Em breve

# Executando

## Com Simulador
Há um arquivo de auxílio para rodar o simulador. Para compilá-lo, entre no diretório vss-simulator e rode o comando make.<br>
Depois de compilado o programa pode ser rodado pelo comando:
```
$ ./Simulador
```
A simulação cria um arquivo de log com as saídas dos programas de simulação para serem analisados.

## Com Sistemas de Visão e Hardware reais
Em breve.

# Padrões de código

## Primeiro comentário do arquivo

    """ Nome do módulo :
        Ano de criação :
        Descrição do módulo :
        Versão :
        Pré-requisitos : (arquivos e bibliotecas necessárias para compilar)
        Membros :
    """


## Comentário de protótipo de funções

    """ Nome da função :
        Intenção da função :
        Pré-requisitos :
        Efeitos colaterais :
        Parâmetros :
        Retorno :
    """
    

**IMPORTANTE**: Comentários adicionais devem ser feitos na implementação (corpo das funções) detalhando a implementação do código.

# Dados da Equipe:
O VSSS-ERUS é uma equipe dedicada a implementação do desafio Very Small Size Soccer para competições. É um projeto da ERUS - Equipe de Robótica da UFES, e diversos documentos sobre o projeto podem ser encontrados no site da equipe.
- Site da ERUS : http://erus.ufes.br/
- E-mail da ERUS : erus@inf.ufes.br
- E-mail do VSSS-ERUS : vssserus@gmail.com

## Membros Atuais
- Gabriel Pietroluongo
    - gabrielpietroluongo@gmail.com
- Gabriel Valdino
    - gvaldino@yahoo.com
- Mayke Wallace
    - mayke.ace@hotmail.com
- Lara de Luca
    - lara2058@hotmail.com
- Lorena Bassani
    - lorenabassani12@gmail.com

## Membros Antigos
- Ricardo Ramos
    - ricardobraun20006@gmail.com
- Victor de Oliveira
    - makkakie97@gmail.com
