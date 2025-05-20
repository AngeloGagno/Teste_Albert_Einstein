from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import urllib



class Config:
    '''Configuração inicial do Banco de Dados - Criação de Engine(através da URL do Banco).
            Métodos:
                engine_creator: Instância que retorna a Engine do banco criada
                get_db: Cria uma sessão no banco de dados para realização do processo de CRUD
    '''
    def __init__(self):
        _ = load_dotenv(override=True)
        #Parametros para execução do SQL Server
        params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={os.getenv('DB_HOST')},1433;"
    f"DATABASE={os.getenv('DATABASE')};"
    f"UID={os.getenv('USER')};"
    f"PWD={os.getenv('PASSWORD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes"
)
        self.engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    
    def _start_session(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def engine_creator(self):
        return self.engine
    
    def get_db(self):
        SessionLocal = self._start_session()
        db = SessionLocal() 
        try:
            yield db
        finally:
            db.close()
