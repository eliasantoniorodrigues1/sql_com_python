import pyodbc
from math import ceil


def string_conexao():
    # Dados da conexao com o Banco
    driver_sql = '{SQL Server}'
    server = 'SERVIDOR'
    database = 'BANCO_DE_DADOS'
    user = 'usuario'
    psw = 'senha'
    string_de_conexao = f"DRIVER={driver_sql};SERVER={server};DATABASE={database};USER ID={user};PASSWORD={psw}"
    return string_de_conexao


def conectar(string_conexao):
    conexao = pyodbc.connect(string_conexao, autocommit=True)
    return conexao


def executa_sql(conexao, query, *args):
    # Essa função aceita uma query com argumentos do tipo
    # where nome in (?) e ai você passa uma lista com os paramêtros.
    with conexao as cursor:
        if args != None:
            r = cursor.execute(query, *args)
        else:
            r = cursor.execute(query)
    return r


def txt_query(arq_caminho_completo):
    with open(arq_caminho_completo, 'r') as arquivo:
        query = arquivo.read()
    return query


def divide_insert(lista, inicio, passo):
    # Essa função recebe uma lista contendo os values do seu insert
    # inicio e passo, para dividir em uma sublista para fazer insert
    # por lotes. Exemplo realizar um insert de 1000 em 1000
    # inicio = 0 passo = 1000
    tamanho = len(lista)
    fim = passo
    qtde = ceil(len(lista) / passo)
    lista_consolidada = []
    lista_to_insert = []
    total = 0

    for i in range(qtde):
        if fim > tamanho:
            fim = tamanho

        lista_to_insert = lista[inicio:fim]
        total += len(lista_to_insert)

        lista_consolidada.append(lista_to_insert[:])
        lista_to_insert.clear()

        inicio = fim
        fim += passo
    return lista_consolidada, total


def executa_insert(cursor, banco_de_dados, tabela, *args):
    # Função que irá receber um cursor de conexão, nome do banco e tabela e uma
    # tupla contendo os argumentos.
    colunas = ','.join([str(coluna).strip().replace(
        '\n', '').replace('\r', '') for coluna in args])
    query = f'INSERT INTO [RH_RPA].[dbo].[{tabela}] VALUES {colunas}'
    print(query)
    cursor.execute(query)
    cursor.commit()


def truncate_table(cursor, banco_de_dados, tabela):
    cursor.execute(f'TRUNCATE TABLE [{banco_de_dados}].[dbo].[{tabela}]')
    cursor.commit()
