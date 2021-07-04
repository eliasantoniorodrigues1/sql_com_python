# SQL_com_python
Esse repositório foi criado para ajudar você que está precisando de executar instruções SQL em seus scripts Python. O objetivo dele é facilitar a execução de selects e inserts em seu banco de dados e de quebra pode te ajudar quando precisar que seu usuário final execute uma tarefa no banco sem ter acesso a ele.

# Funções do Repositório
Esse repositório possui diversas funções que eu utilizo muito no meu dia a dia de trabalho.

# Insert Automático
A função de insert automático está no módulo conexao_bd e funciona da seguinte maneira:
Recebe um cursor, nome do banco de dados, tabela e uma lista de argumentos
Após isso é montado uma instrução SQL que irá tratar os dados e preparar o comando para o insert.

def executa_insert(cursor, banco_de_dados, tabela, *args):
    # Função que irá receber um cursor de conexão, nome do banco e tabela e uma
    # tupla contendo os argumentos.
    colunas = ','.join([str(coluna).strip().replace(
        '\n', '').replace('\r', '') for coluna in args])
    query = f'INSERT INTO [RH_RPA].[dbo].[{tabela}] VALUES {colunas}'
    print(query)
    cursor.execute(query)
    cursor.commit()
    
 # Remove acentos
 Função estudada e aprendida no artigo do Luiz Otávio Miranda e resolvi adicionar ao módulo Utils, uma funcionalidade que utilizo muito.
 https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/comment-page-1/?unapproved=533&moderation-hash=328074af6087c8b0ef51de4cfb7a92ad#top
 
 # Observação
 Analisar os demais modulos desse repositório e em caso de dúvidas ou sugestões estou a disposição.
