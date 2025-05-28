import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os


def conectar_banco(nome_banco='database.db'):
    return sqlite3.connect(nome_banco)


def criar_tabelas(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id_venda INTEGER PRIMARY KEY,
            produto TEXT,
            quantidade INTEGER,
            valor_total REAL,
            data_venda DATE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            cidade TEXT
        )
    ''')

    conn.commit()


def carregar_dados(conn):
    if os.path.exists('dados/vendas.csv'):
        df_vendas = pd.read_csv('dados/vendas.csv')
        df_vendas.to_sql('vendas', conn, if_exists='replace', index=False)
    else:
        print("Arquivo 'dados/vendas.csv' não encontrado.")

    if os.path.exists('dados/clientes.json'):
        df_clientes = pd.read_json('dados/clientes.json')
        df_clientes.to_sql('clientes', conn, if_exists='replace', index=False)
    else:
        print("Arquivo 'dados/clientes.json' não encontrado.")


def produto_mais_vendido(cursor):
    query = '''
        SELECT produto, SUM(quantidade) AS total_quantidade
        FROM vendas
        GROUP BY produto
        ORDER BY total_quantidade DESC
        LIMIT 1
    '''
    cursor.execute(query)
    resultado = cursor.fetchone()
    if resultado:
        print(f"Produto mais vendido: {resultado[0]} ({resultado[1]} unidades)")
    else:
        print("Nenhuma venda registrada.")


def total_vendas_por_produto(conn):
    query = '''
        SELECT produto, SUM(valor_total) as total_vendas
        FROM vendas
        GROUP BY produto
    '''
    df = pd.read_sql_query(query, conn)
    print("\nTotal de vendas por produto:\n", df)
    return df


def filtrar_vendas_por_data(conn, data_inicio, data_fim):
    query = '''
        SELECT * FROM vendas
        WHERE data_venda BETWEEN ? AND ?
    '''
    df = pd.read_sql_query(query, conn, params=(data_inicio, data_fim))
    print(f"\nVendas entre {data_inicio} e {data_fim}:\n", df)
    return df


def gerar_grafico(df):
    plt.figure(figsize=(8, 6))
    plt.bar(df['Produto'], df['total_vendas'], color='skyblue')
    plt.title('Total de Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Valor Total (R$)')
    plt.tight_layout()
    plt.savefig('total_vendas_por_produto.png', dpi=300)
    plt.show()


def media_vendas_por_dia(conn):
    query = '''
        SELECT data_venda, AVG(valor_total) as media_vendas
        FROM vendas
        GROUP BY data_venda
    '''
    df = pd.read_sql_query(query, conn)
    print("\nMédia de vendas por dia:\n", df)
    return df


def main():
    try:
        conn = conectar_banco()
        cursor = conn.cursor()

        criar_tabelas(conn)
        carregar_dados(conn)

        produto_mais_vendido(cursor)

        df_vendas_totais = total_vendas_por_produto(conn)

        filtrar_vendas_por_data(conn, '2024-01-06', '2024-01-08')

        gerar_grafico(df_vendas_totais)

        media_vendas_por_dia(conn)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
