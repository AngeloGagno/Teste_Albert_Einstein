# src/frontend/csv_uploader.py
import streamlit as st
import pandas as pd
from transform.disease_table import Pipeline_transform_disease_table


class CSVUploader:
    def __init__(self, engine, table_name: str, label="Escolha um arquivo CSV", file_types=["csv"]):
        st.set_page_config(page_title="Uploader CSV com Transformação", layout="wide")
        self.label = label
        self.file_types = file_types
        self.table_name = table_name
        self.engine = engine
        self.dataframe = None
        
    def upload(self):
        ''' Recebe um arquivo CSV do usuario para carregamento, tratamento e envio ao banco'''
        uploaded_file = st.file_uploader(self.label, type=self.file_types)
        if uploaded_file:
            try:
                self.dataframe = pd.read_csv(uploaded_file,sep=';')
                st.success("Arquivo carregado com sucesso!")
                return True
            except Exception as e:
                st.error(f"Erro ao ler o arquivo: {e}")
        else:
            st.info("Por favor, envie um arquivo CSV.")
        return False

    def transformed_dataframe(self):
        ''' Função que executa o tratamento de dados da tabela disease'''
        return Pipeline_transform_disease_table(self.dataframe).pipeline()
    
    def show_preview(self):
        ''' Exibe os 5 primeiros valores do dataframe tratado para verificação do usuario'''
        if self.dataframe is not None:
            st.subheader("Pré-visualização dos dados")
            st.dataframe(self.transformed_dataframe().head(5))

    def insert_to_db(self):
        ''' Envia os dados para o banco e retorna erro caso o dado ja exista'''
        if self.transformed_dataframe() is not None:
            try:
                self.transformed_dataframe().to_sql(
                    name=self.table_name,
                    con=self.engine,
                    if_exists='append',
                    index=False
                )
                st.success(f"{len(self.transformed_dataframe())} registros inseridos na tabela '{self.table_name}'.")
            except Exception as e:
                st.error(f"Erro ao inserir dados no banco: {e}")