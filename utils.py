import socket
import unicodedata
import re
import getpass
import datetime
import csv


def remove_acentos(string):
    normalizado = unicodedata.normalize('NFKD', string)
    return ''.join([c for c in normalizado if not unicodedata.combining(c)])


def remove_non_digit(str):
    return re.sub(r'\D', '', str)


def grava_log(caminho_completo, conteudo):
    with open(caminho_completo, 'w') as file:
        if conteudo != '':
            for linha in conteudo:
                file.write(linha)
                file.write('\n')
        else:
            file.write('Não há dados para serem gravados.')
            file.write('\n')


def dados_sessao_windows():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    user = getpass.getuser()
    return hostname, local_ip, user


def cria_csv(caminho, nome, lista_cabecalho, lista_conteudo):
    caminho_completo = os.path.join(caminho, nome, '.csv')
    with open(caminho_completo, 'w') as arquivo:
        escreve = csv.writer(
            tabela_log,
            delimiter=';'
            # Mais parâmetros podem ser adicionados nessa
            # seção.
        )
        if len(lista_conteudo) > 0:
            escreve.writerow(lista_cabecalho)
            for dado in lista_conteudo:
                escreve.writerow(dado)
                escreve.writerow('\n')


def data_agora_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def envia_email(fom, to, content):
    ...


if __name__ == '__main__':
    texto = 'EÇOALHO caroço até joão avô'
    print(remove_acentos(texto))
