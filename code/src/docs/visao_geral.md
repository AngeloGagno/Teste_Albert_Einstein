# Visão Geral

Este sistema foi desenvolvido para processar e armazenar dados de saúde pública, utilizando um pipeline ETL (Extração, Transformação e Carga) com as seguintes etapas principais:

- **Extração:** Leitura de arquivos CSV contendo dados brutos.
- **Transformação:** Limpeza, padronização e preparação dos dados para o banco de dados.
- **Carga:** Inserção dos dados tratados em um banco SQL Server.
- **Frontend:** Interface web para upload, visualização e envio dos dados, construída com Streamlit.

A arquitetura é modular, separando as responsabilidades em diferentes diretórios:
- `extract/`: Extração de arquivos CSV.
- `transform/`: Pipelines de limpeza e transformação de dados.
- `database/`: Modelos e configuração do banco de dados.
- `frontend/`: Interface de upload e visualização.

O sistema é configurável via variáveis de ambiente e utiliza o Poetry para gerenciamento de dependências. 