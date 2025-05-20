from extract.generic_csv_extracter import GetFiles
from transform.disease_table import Pipeline_transform_disease_table

from database.db import Config
from database.models import *

import streamlit as st
from frontend.app import CSVUploader

def executar_pipeline_e_insercao():
    uploader = CSVUploader(engine=Config().engine_creator(), table_name='diseaseSummary',title='Sistema de Insersão de dados')

    if uploader.upload():
        uploader.show_preview()

        if st.button("Transformar dados e Inserir no banco"):
            uploader.insert_to_db()

def send_to_db():
    Base.metadata.create_all(bind=Config().engine_creator()) # Cria o banco caso ele não exista
    executar_pipeline_e_insercao()

if __name__ == '__main__':
    send_to_db()