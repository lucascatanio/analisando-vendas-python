import sqlite3  # Banco SQLite
import pandas as pd  # Manipulação de dados
import matplotlib.pyplot as plt  # Gráficos


def criar_conexao(db_name='database.db'):
    """
    Cria conexão com o banco SQLite.
    Retorna objeto conexão e cursor.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor


def criar_tabelas(cursor):
    """
    Cria tabelas vendas e clientes se não existirem.
    """
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id_venda INTEGER,
            produto TEXT,
            quantidade INTEGER,
            valor_total REAL,
            data_venda TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER,
            nome TEXT,
            cidade TEXT
        )
    ''')


def importar_dados(conn):
    """
    Importa dados de CSV e JSON para as tabelas vendas e clientes.
    Substitui os dados existentes.
    """
    # Lê CSV de vendas
    df_vendas = pd.read_csv('dados/vendas.csv')
    df_vendas.to_sql('vendas', conn, if_exists='replace', index=False)

    # Lê JSON de clientes
    df_clientes = pd.read_json('dados/clientes.json')
    df_clientes.to_sql('clientes', conn, if_exists='replace', index=False)


def produto_mais_vendido(cursor):
    """
    Consulta e retorna o produto mais vendido (quantidade).
    """
    query = '''
        SELECT produto, SUM(quantidade) AS total_quantidade
        FROM vendas
        GROUP BY produto
        ORDER BY total_quantidade DESC
        LIMIT 1
    '''
    cursor.execute(query)
    return cursor.fetchone()


def total_vendas_por_produto(conn):
    """
    Consulta o total vendido por produto (valor monetário).
    Retorna um DataFrame pandas.
    """
    query = '''
        SELECT produto, SUM(valor_total) as total_vendas
        FROM vendas
        GROUP BY produto
    '''
    return pd.read_sql_query(query, conn)


def vendas_por_periodo(conn, data_inicio, data_fim):
    """
    Consulta vendas entre duas datas.
    Retorna DataFrame.
    """
    query = '''
        SELECT * FROM vendas
        WHERE data_venda BETWEEN ? AND ?
    '''
    return pd.read_sql_query(query, conn, params=(data_inicio, data_fim))


def gerar_grafico_vendas(df_total_vendas):
    """
    Gera e salva gráfico de barras do total de vendas por produto.
    """
    plt.figure(figsize=(8,6))
    plt.bar(df_total_vendas['produto'], df_total_vendas['total_vendas'], color='skyblue')
    plt.title('Total de Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Valor Total (R$)')
    plt.savefig('grafico_vendas.png', dpi=300)
    plt.show()


def media_vendas_por_dia(conn):
    """
    Consulta e retorna a média diária de vendas.
    """
    query = '''
        SELECT data_venda, AVG(valor_total) as media_vendas
        FROM vendas
        GROUP BY data_venda
    '''
    return pd.read_sql_query(query, conn)


def main():
    # Criar conexão e cursor
    conn, cursor = criar_conexao()

    # Criar tabelas
    criar_tabelas(cursor)
    conn.commit()  # Salvar estrutura no banco

    # Importar dados de arquivos para o banco
    importar_dados(conn)

    # Produto mais vendido
    prod = produto_mais_vendido(cursor)
    print(f"Produto mais vendido: {prod[0]} ({prod[1]} unidades)")

    # Total de vendas por produto
    df_total = total_vendas_por_produto(conn)
    print("\nTotal de vendas por produto:\n", df_total)

    # Vendas em intervalo de datas
    inicio = '2024-01-06'
    fim = '2024-01-08'
    df_filtrado = vendas_por_periodo(conn, inicio, fim)
    print(f"\nVendas entre {inicio} e {fim}:\n", df_filtrado)

    # Gerar gráfico
    gerar_grafico_vendas(df_total)

    # Média de vendas por dia
    df_media = media_vendas_por_dia(conn)
    print("\nMédia de vendas por dia:\n", df_media)

    # Fechar conexão
    conn.close()


if __name__ == "__main__":
    main()
