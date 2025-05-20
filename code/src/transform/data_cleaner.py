import pandas as pd

class GenericCleaner:
    def __init__(self,dataframe:pd.DataFrame) -> None:
        self.df = dataframe

    def column_remover(self, columns: list):
        '''Removedor de colunas do dataframe'''
        self.df = self.df.drop(columns=columns)
        return self.df

    def replace_data_row(self,column:str,data_to_replace:str,replace:str) -> pd.DataFrame:
        '''Realizar a limpeza dos dados'''
        self.df[column] = self.df[column].str.replace(data_to_replace,replace)
        return self.df

    def null_cleaner(self,column:str,filler) -> pd.DataFrame:
        '''Altera os valores nulos pelo desejado'''
        self.df[column] = self.df[column].fillna(filler)
        return self.df
    
    def change_type(self,column:str,type:str) -> pd.DataFrame:
        '''Altera o tipo da coluna'''
        self.df[column] = self.df[column].astype(type)
        return self.df

    def change_data_from_rows(self,column:str,values:dict) -> pd.DataFrame:
        self.df[column] = self.df[column].replace(values)
        return self.df

    def refactor_columns_name(self, old_name, new_name) -> pd.DataFrame:
        self.df.rename(columns={old_name: new_name}, inplace=True)