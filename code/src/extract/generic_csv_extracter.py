from pathlib import Path
import pandas as pd

class GetFiles:
    def __init__(self,file_name:str) -> None:
        self.path = self.path(file_name)
        self.folders = self.fetch_all_folders()

    def path(self,file_name:str):
        '''Retorna o caminho da pasta onde contem os arquivos csv'''
        actual_path = Path.cwd()
        return actual_path.parents[1] / file_name

    def fetch_all_folders(self):
        '''Acessa a pasta que contem os arquivos csv e retorna uma lista com todos'''
        path = self.path
        return [str(folder) for folder in path.rglob("*.csv")]
            
    def merge_and_delete_csvs(self,sep=',',encode= 'UTF-8'):
        '''Une os arquivos CSV contidos na pasta que contem os arquivos csv'''
        csv_files = self.fetch_all_folders()
        if not csv_files:
            print("Nenhum arquivo CSV encontrado.")
            return None
        dfs = [pd.read_csv(file,sep=sep,encoding=encode) for file in csv_files]
        df_final = pd.concat(dfs, ignore_index=True)

        return df_final
