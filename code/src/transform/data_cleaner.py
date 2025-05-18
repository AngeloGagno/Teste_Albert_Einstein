import pandas as pd

class GenericCleaner:
    def __init__(self,dataframe:pd.DataFrame) -> None:
        self.df = dataframe

    def column_remover(self,columns:list):
        '''Removedor de colunas do dataframe'''
        return self.df.drop(columns=columns)
    
    def null_cleaner(self,column,filler):
        '''Altera os valores nulos pelo desejado'''
        return self.df[column].fillna(filler)
    
    def change_type(self,column,type):
        '''Altera o tipo da coluna'''
        return self.df[column].astype(type)