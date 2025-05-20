# Pipeline ETL

## Extração
A extração dos Municípios realizada por meio da classe `GetFiles` em `extract/generic_csv_extracter.py`, que localiza e lê arquivos CSV de uma pasta específica e a extração da tabela de doenças é feita por meio do [Frontend]()

## Transformação
A transformação dos dados é feita por pipelines dedicados:
- `Pipeline_transform_disease_table` (em `transform/disease_table.py`): Limpa, padroniza e renomeia colunas dos dados de doenças.
- `Pipeline_transform_municipios_table` (em `transform/district_table.py`): Padroniza e limpa dados de municípios.
- Utiliza utilitários de limpeza em `transform/data_cleaner.py`.

## Carga
A carga dos dados é feita utilizando o Streamlit que insere os DataFrames tratados nas tabelas do banco SQL Server.

## Scripts Principais
- `streamlit run main.py`: Executa o pipeline completo para dados de doenças.
- `insert_municipios.py`: Executa o pipeline para dados de municípios.
