# AWS Sales Data Pipeline

Projeto de estudo em Engenharia de Dados desenvolvido para praticar um fluxo de processamento e análise de dados utilizando Python, Pandas, SQL e PySpark, com futura integração com serviços AWS.

## Objetivo

Construir um pipeline simples de dados a partir de um dataset de vendas, passando por etapas de:

* ingestão de dados
* limpeza e validação
* armazenamento
* análise exploratória
* consultas SQL
* processamento com PySpark
* integração futura com AWS

## Tecnologias

* Python
* Pandas
* PySpark
* SQL
* SQLite
* Matplotlib
* AWS S3 / Glue / Athena *(etapa futura)*

## Estrutura

```text
aws/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── ingestion/
│   ├── transformation/
│   ├── validation/
│   └── analysis/
├── sql/
├── notebooks/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## Pipeline atual

```text
CSV
 ↓
Python / Pandas
 ↓
Limpeza e validação
 ↓
CSV processado
 ↓
SQLite
 ↓
SQL / Análise exploratória
 ↓
PySpark
```

A integração com AWS será adicionada posteriormente.

## Principais análises

O projeto atualmente realiza análises como:

* faturamento mensal
* vendas e lucro por categoria
* relação entre desconto e lucro médio
* desempenho de produtos
* desempenho por região
* métricas gerais de vendas

Também são utilizadas consultas SQL com:

* `JOIN`
* agregações
* `GROUP BY`
* CTEs
* Window Functions

## Como executar

Clone o repositório e instale as dependências:

```bash
git clone <URL_DO_REPOSITORIO>
cd aws
python3 -m pip install -r requirements.txt
```

Para executar a limpeza dos dados:

```bash
python3 -m src.ingestion.explore_data
```

Para carregar os dados no SQLite:

```bash
python3 -m src.ingestion.load_database
```

Para executar as análises SQL:

```bash
python3 -m src.analysis.run_sql
```

Para executar a análise exploratória:

```bash
python3 -m src.analysis.sales_analysis
```

## Observações

O dataset utilizado é mantido localmente e não é versionado no Git, conforme definido no `.gitignore`.

Este projeto está sendo desenvolvido como parte do estudo de Engenharia de Dados, com foco em Python, análise de dados, processamento distribuído e serviços de dados em nuvem.
