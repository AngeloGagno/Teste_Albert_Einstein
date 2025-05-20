# Configuração

## Requisitos
- Python 3.13+
- SQL Server (pode ser local ou em container Docker)
- Poetry (para gerenciamento de dependências)

## Instalação
1. Clone o repositório e acesse a pasta do projeto.
2. Instale as dependências:
   ```bash
   poetry install
   ```
3. Copie o arquivo `env-example` para `.env` e preencha com as credenciais do banco:
   ```env
   DB_HOST=HOSTNAME
   DATABASE=master
   USER=username
   PASSWORD=password
   ```

## Execução
- Para acessar o frontend para envio das cargas de dados:
   frontend
- Para inserir dados de municípios:
  ```bash
  poetry run python src/insert_municipios.py
  ```