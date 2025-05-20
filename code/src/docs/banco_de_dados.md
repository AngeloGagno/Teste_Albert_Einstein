# Banco de Dados

O sistema utiliza um banco de dados SQL Server para armazenar os dados processados. A conexão é configurada via SQLAlchemy e as credenciais são definidas por variáveis de ambiente.

## Modelos Principais

### DiseaseTable (`diseaseSummary`)
Tabela principal para dados de doenças, com colunas para informações demográficas, localização, sintomas, condições, vacinação, testes e datas relevantes.

### DistrictTable (`municipios`)
Tabela de municípios baseada no [IBGE](https://www.ibge.gov.br/), contendo códigos e nomes de regiões, estados e municípios.

## Definição das Tabelas
Os modelos estão definidos em `database/models.py` e são criados automaticamente pelos scripts do pipeline.

Consulte o código para detalhes de cada campo e tipos de dados. 