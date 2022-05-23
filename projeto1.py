from cmath import inf
import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    categorias = []
    for dado in dados:
        if dado['categoria'] not in categorias:
            categorias.append(dado['categoria'])
    return sorted(categorias)
    
def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    produtos = []
    for dado in dados:
        if dado['categoria']==categoria:
            produtos.append(dado)
    return produtos
    

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    mais_caro = {}
    max_preco = 0
    for dado in dados:
        if dado['categoria']==categoria:
            if float(dado['preco']) > max_preco:
                max_preco = float(dado['preco'])
                mais_caro = dado
    return mais_caro



def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais barato da categoria dada.
    '''
    mais_barato = {}
    min_preco = 9999999999999999
    for dado in dados:
        if dado['categoria']==categoria:
            if float(dado['preco']) < min_preco:
                min_preco = float(dado['preco'])
                mais_barato = dado
    return mais_barato

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    return sorted(dados, key = lambda x: float(x["preco"]), reverse = True)[0:10]


def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    return sorted(dados, key = lambda x: float(x["preco"]))[0:10]

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    entrada = ''
    while entrada != '0':
        print('\n\n\n            1. Listar categorias \n\
            2. Listar produtos de uma categoria\n\
            3. Produto mais caro por categoria\n\
            4. Produto mais barato por categoria\n\
            5. Top 10 produtos mais caros\n\
            6. Top 10 produtos mais baratos\n\
            0. Sair\n\n\n')
        entrada = input('Digite a sua opção:  ')

        if entrada == '1':
            print("\n\nCATEGORIAS DISPONÍVEIS: \n")
            for categoria in listar_categorias(dados):
                print(categoria)
        elif entrada == '2':
            categoria = input('Qual a categoria desejada?  ')
            while categoria not in listar_categorias(dados):
                categoria = input('\nOpção inválida! Selecione outra categoria!\n')
            else:
                print('\nLISTA DE PRODUTOS DA CATEGORIA', categoria.upper())
                for produto in listar_por_categoria(dados, categoria):
                    print('O produto de id: ',produto["id"],'possui preço de R$',produto['preco'],'e pertence a categoria:', produto["categoria"])
        elif entrada == '3':
            categoria = input('Qual a categoria desejada?  ')
            while categoria not in listar_categorias(dados):
                categoria = input('\nOpção inválida! Selecione outra categoria!\n')
            else:
                print('\nO produto mais caro da categoria',produto_mais_caro(dados, categoria)["categoria"],'é o de id: ',produto_mais_caro(dados, categoria)["id"],'com o preço de R$',produto_mais_caro(dados, categoria)['preco'])
        elif entrada == '4':
            categoria = input('Qual a categoria desejada?  ')
            while categoria not in listar_categorias(dados):
                categoria = input('\nOpção inválida! Selecione outra categoria!\n')
            else:
                print('\nO produto mais barato da categoria',produto_mais_barato(dados, categoria)["categoria"],'é o de id: ',produto_mais_barato(dados, categoria)["id"],'com o preço de R$',produto_mais_barato(dados, categoria)['preco'])
        elif entrada == '5':
            print('\nLISTA DE PRODUTOS MAIS CAROS:')
            for top in top_10_caros(dados):
                print('O produto de id: ',top["id"],'possui preço de R$',top['preco'],'e pertence a categoria:', top["categoria"])
        elif entrada == '6':
            print('\nLISTA DE PRODUTOS MAIS BARATOS:')
            for top in top_10_baratos(dados):
                print('O produto de id: ',top["id"],'possui preço de R$',top['preco'],'e pertence a categoria:', top["categoria"])          
        elif entrada == '0':
            break;
        else:
            print('\nEntrada inválida! Escolha outra opção.\n')

    


# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)

