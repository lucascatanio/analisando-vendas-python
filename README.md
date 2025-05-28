# 📊 Sistema de Análise de Vendas com SQLite, Pandas e Matplotlib

Este projeto é um mini sistema de análise de vendas utilizando Python. Ele integra um banco de dados SQLite com dados importados de arquivos CSV e JSON, realiza consultas SQL e gera visualizações gráficas dos resultados.

---

## 🚀 Funcionalidades

- 📥 Leitura de dados de vendas (CSV) e clientes (JSON)
- 🗃️ Armazenamento em banco de dados SQLite
- 🔎 Consultas SQL para análise de dados:
  - Produto mais vendido
  - Total de vendas por produto
  - Vendas por intervalo de datas
  - Média de vendas por dia
- 📊 Geração de gráfico de barras com `matplotlib`
- 🖼️ Salvamento do gráfico como imagem PNG

---

## 📂 Estrutura de Pastas

```
.
├── dados/
│   ├── vendas.csv
│   └── clientes.json
├── database.db
├── grafico_vendas.png
├── main.py
├── README.md
└── .gitignore
```

---

## 🛠️ Requisitos

- Python 3.8+
- Bibliotecas:
  - `pandas`
  - `matplotlib`

### Instalar dependências:

```bash
pip install pandas matplotlib
```

---

## ▶️ Como executar

```bash
python main.py
```

---

## 📈 Exemplo de saída

- Produto mais vendido com total de unidades
- Tabela com total de vendas por produto
- Tabela com vendas em intervalo de datas
- Gráfico gerado: `grafico_vendas.png`

---

## 📌 Observações

- Os dados de entrada devem estar na pasta `dados/` com os nomes:
  - `vendas.csv`
  - `clientes.json`
- O banco de dados será criado como `database.db`.

---

## 📝 Licença

Este projeto é de uso educacional e está disponível sob a licença MIT.
