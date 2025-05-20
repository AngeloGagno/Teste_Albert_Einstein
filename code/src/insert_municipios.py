
from transform.district_table import Pipeline_transform_municipios_table
from extract.generic_csv_extracter import GetFiles
from database.db import Config
from database.models import *
import pandas as pd

def pipeline_df_districts():
    '''Pipeline de extração e tratamento dos dados da tabela de municipios'''
    df_districts = GetFiles('tabela_municipios').merge_and_delete_csvs(sep=';',encode='latin1')
    df_districts_cleaned = Pipeline_transform_municipios_table(df_districts).pipeline()
    return df_districts_cleaned

def sent_to_db():
    ''' Enviar os dados estaticos de municípios para o banco de dados.'''
    Base.metadata.create_all(bind=Config().engine_creator())
    pipeline_df_districts().to_sql('municipios',con=Config().engine_creator(),if_exists='append',index_label=False)

if __name__ == '__main__':
    sent_to_db()