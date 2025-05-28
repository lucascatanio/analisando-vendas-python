# Análise de Vendas com SQLite, Pandas e Matplotlib

Este projeto realiza uma análise simples de dados de vendas utilizando:

- SQLite para armazenar os dados
- Pandas para manipulação e consulta
- Matplotlib para geração de gráficos

## Funcionalidades

- Criação de banco de dados e tabelas
- Importação de dados de arquivos CSV e JSON
- Consultas SQL para análises
- Geração de gráfico de vendas por produto
- Cálculo de média de vendas por dia

## Como executar

1. Certifique-se de ter Python 3 instalado.
2. Instale as dependências com:
   ```
   pip install pandas matplotlib
   ```
3. Execute o script:
   ```
   python main.py
   ```

## Resultado

- Exibição de dados no terminal
- Geração de gráfico `grafico_vendas.png`
- Exemplo de uso real de SQLite + Pandas + Matplotlib

## Licença

---

## Simulador de Temperatura (`streaming_simulacao.py`)

Este script simula a leitura de temperatura de um sensor em tempo real.

- A cada 2 segundos, uma nova leitura aleatória entre 50°C e 90°C é gerada.
- Se a temperatura ultrapassar 70°C, um alerta é emitido e salvo no arquivo `alertas.txt`.

### Como executar

```bash
python streaming_simulacao.py
```

### Saída

- Leituras contínuas no terminal.
- Arquivo `alertas.txt` contendo os registros de temperatura acima do limite.

Para encerrar a simulação, use `Ctrl+C`.
