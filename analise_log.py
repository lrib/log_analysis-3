"""
    Projeto de analise de logs
    Este codigo realiza a extracao dos dados sumarizados
    do bando de dados que apresenta um log
    de cadastro e acesso a um site de noticias
"""
import psycopg2
import pycodestyle
from prettytable import PrettyTable
# Define o nome da base de dados
DBNAME = "news"


def impr_top_artigos():
    """
    Cria a funcao que ira abrir a base de dados,
    fazer o query e apresentar a 1 questao
    """
    # analisa se vai ocorrer algum erro na abertura da base de dado
    try:
        # abra a base de dados 'news'
        basededados = psycopg2.connect(database=DBNAME)

        cursor = basededados.cursor()
        # monta a requisicao SQL
        primeiro_query = " select articles.title, count(log.path) from log \
                      join articles on log.path like '%' || articles.slug \
                      group by articles.title order by count desc limit 3; "
        # executa a requisicao SQL
        cursor.execute(primeiro_query)
        # copia o resultado para a variavel
        primeira_gravacao = cursor.fetchall()
        # inicializa a tabela de apresentacao do resultado
        x = PrettyTable()
        # cria o cabecalho da tabela
        x.field_names = ["Artigo", "Numero de visualizacoes"]

        print('1.Quais sao os tres artigos mais populares de todos os tempos:')
        # Faz um loop no resuldato do query para apresenta-los
        for linha in primeira_gravacao:
            # fica no loop, copiando o resultado para a tabela a ser impressa
            x.add_row([linha[0], linha[1]])
        # ao sair do loop imprime o resultado
        print(x)
        # converte todo a tabela com carcteres string
        data = str(x)
    # se ocorreu algum erro na abertura da base de dados, entra aqui.
    except (Exception, psycopg2.Error) as error:
        # imprime a msg de erro e o erro
        print ("Erro ao buscar dados do PostgreSQL", error)
    # retorna a tabela
    else:
        return data


def impr_top_autores():
    """
    Cria a funcao que ira abrir a base de dados,
    fazer o query e apresentar a 2 questao
    """
    # analisa se vai ocorrer algum erro na abertura da base de dado
    try:
        # abra a base de dados 'news'
        basededados = psycopg2.connect(database=DBNAME)

        cursor = basededados.cursor()
        # monta a requisicao SQL
        primeiro_query = "select authors.name, count(log.path) from log\
                          join articles on log.path like '%' || articles.slug\
                          join authors on authors.id = articles.author\
                          group by authors.name order by count desc "
        # executa a requisicao SQL
        cursor.execute(primeiro_query)
        # copia o resultado para a variavel
        primeira_gravacao = cursor.fetchall()
        # inicializa a tabela de apresentacao do resultado
        x = PrettyTable()
        # cria o cabecalho da tabela
        x.field_names = ["Autor", "Numero de visualizacoes"]

        print('2.Quais sao os atores mais populares de todos os tempos:')
        # Faz um loop no resuldato do query para apresenta-los
        for linha in primeira_gravacao:
            # fica no loop, copiando o resultado para a tabela a ser impressa
            x.add_row([linha[0], linha[1]])
        # imprime a tabela
        print(x)
        # converte todo a tabela com carcteres string
        data = str(x)
    # se ocorreu algum erro na abertura da base de dados, entra aqui.
    except (Exception, psycopg2.Error) as error:
        # imprime a msg de erro e o erro
        print ("Erro ao buscar dados do PostgreSQL", error)
    # retorna a tabela
    else:
        return data


def impr_top_erros():
    """
    Cria a funcao que ira abrir a base de dados,
    fazer o query e apresentar a 3 questao
    """
    # analisa se vai ocorrer algum erro na abertura da base de dado
    try:
        # abra a base de dados 'news'
        basededados = psycopg2.connect(database=DBNAME)

        cursor = basededados.cursor()
        # monta a requisicao SQL
        primeiro_query = "select total.dadosok, erro.dadoserr, total.dia, \
                          round((erro.dadoserr::numeric \
                          * 100::numeric / total.dadosok::numeric),2)\
                          from ( select CAST(l.time AS DATE) as dia, \
                          (count(l.status)) as dadosok from log as l \
                          group by CAST(l.time AS DATE)) as total join \
                          (  select CAST(time AS DATE) as dia, \
                          (count(status)) as dadoserr from log \
                          where status not like '%200%' \
                          group by CAST(time AS DATE) ) as erro \
                          ON total.dia = erro.dia \
                          where erro.dadoserr::numeric * \
                          100::numeric / total.dadosok::numeric > 1;"
        # executa a requisicao SQL
        cursor.execute(primeiro_query)
        # copia o resultado para a variavel
        primeira_gravacao = cursor.fetchall()
        # inicializa a tabela de apresentacao do resultado
        x = PrettyTable()
        # cria o cabecalho da tabela
        x.field_names = ["Data(AAAA-MM-DD)", "Total Erros(%)",
                         "Total de Acessos", "Total de Erros"]

        print('3.Qual o dia com mais de 1% de erro:')
        # Faz um loop no resuldato do query para apresenta-los
        for linha in primeira_gravacao:
            # fica no loop, copiando o resultado para a tabela a ser impressa
            x.add_row([linha[2], linha[3], linha[0], linha[1]])
        # imprime a tabela
        print(x)
        # converte todo a tabela com carcteres string
        data = str(x)
    # se ocorreu algum erro na abertura da base de dados, entra aqui.
    except (Exception, psycopg2.Error) as error:
        # imprime a msg de erro e o erro
        print ("Erro ao buscar dados do PostgreSQL", error)
    # retorna a tabela
    else:
        return data


def main():
    # aqui temos o programa principal a inicar
    # cria e/abre o arquivo report_fil.log
    f = open("report_file.log", "w")
    # adiciona uma descricao no arquivo
    f.write('1.Quais sao os tres artigos mais populares de todos os tempos:\n')
    # chama a funcao para imprimir e gravar os principais artigos
    f.write(str(impr_top_artigos()))
    # adiciona uma descricao no arquivo
    f.write('\n2.Quais sao os atores mais populares de todos os tempos:\n')
    # chama a funcao para imprimir e gravar os principais autores
    f.write(str(impr_top_autores()))
    # adiciona uma descricao no arquivo
    f.write('\n3.Qual o dia com mais de 1% de erro:\n')
    # chama a funcao para imprimir os erros
    f.write(str(impr_top_erros()))
    # fecha o arquivo
    f.close()


if __name__ == '__main__':
    main()
