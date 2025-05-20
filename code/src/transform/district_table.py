from .data_cleaner import GenericCleaner
import pandas as pd

class Pipeline_transform_municipios_table(GenericCleaner):
    def __init__(self, dataframe):
        self.df = dataframe
        self.column_mappings = {
            'Código Município Completo': 'codigo_municipio',
            'Nome_Município': 'nome_municipio',
            'UF': 'uf',
            'Nome_UF': 'nome_uf',
            'Região Geográfica Intermediária':'codigo_regiao_geografica_intermediaria',
            'Nome Região Geográfica Intermediária': 'nome_regiao_geografica_intermediaria',
            'Região Geográfica Imediata': 'codigo_regiao_geografica_imediata',
            'Nome Região Geográfica Imediata': 'nome_regiao_geografica_imediata',
            'Mesorregião Geográfica': 'codigo_mesorregiao',
            'Nome_Mesorregião': 'nome_mesorregiao',
            'Microrregião Geográfica': 'codigo_microrregiao',
            'Nome_Microrregião': 'nome_microrregiao'
        }

    def _remove_column(self):
        '''Removendo a coluna Município pois já há uma coluna com correlação alta - Código Município Completo'''
        column = ['Município']
        self.column_remover(columns=column)

    def _rename_columns(self):
        """Padronizar o nome das colunas de acordo com a norma para o SQL"""
        for old_name, new_name in self.column_mappings.items():
            self.refactor_columns_name(old_name, new_name)

        
    def pipeline(self) -> pd.DataFrame:
        '''Execução da Pipeline'''
        self._remove_column()
        self._rename_columns()
        return self.df