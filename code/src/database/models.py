from sqlalchemy import Column, Integer, String, Float, Date, SmallInteger, Boolean
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# DistrictTable.py
class DistrictTable(Base):
    __tablename__ = 'municipios'
    
    codigo_municipio = Column(String(10), primary_key=True)
    nome_municipio = Column(String(100), nullable=False)
    uf = Column(String(2), nullable=False)
    nome_uf = Column(String(50), nullable=False)
    codigo_regiao_geografica_intermediaria = Column(String(6))
    nome_regiao_geografica_intermediaria = Column(String(100))
    codigo_regiao_geografica_imediata = Column(String(7))
    nome_regiao_geografica_imediata = Column(String(100))
    codigo_mesorregiao = Column(String(3))
    nome_mesorregiao = Column(String(100))
    codigo_microrregiao = Column(String(4))
    nome_microrregiao = Column(String(100))

    
class DiseaseTable(Base):
    __tablename__ = 'diseaseSummary'

    source_id = Column(String(20),  primary_key=True)
    
    # Dados demográficos
    sexo = Column(String(20))
    raca_cor = Column(String(50))
    idade = Column(Float)
    
    # Localização
    municipio = Column(String(100))
    estado = Column(String(50))
    municipio_notificacao= Column(String(100))
    estado_notificacao = Column(String(20))
    estado_notificacao_IBGE = Column(String(2))
    # Sintomas e condições
    sintomas = Column(String)
    outros_sintomas = Column(String)
    condicoes = Column(String)
    outras_condicoes = Column(String)
    
    # Profissional e segurança
    profissional_saude = Column(Boolean)
    profissional_seguranca = Column(Boolean)
    cbo = Column(String)
    
    # Evolução e classificação
    evolucao_caso = Column(String(50))
    classificacao_final = Column(String(40))
    
    # Estratégias e triagem
    codigo_estrategia_covid = Column(SmallInteger)
    codigo_busca_ativa_assintomatico = Column(SmallInteger)
    outro_busca_ativa_assintomatico = Column(String(100))
    codigo_triagem_populacao_especifica = Column(Float)
    outro_triagem_populacao_especifica = Column(String(100))
    codigo_local_realizacao_testagem = Column(Float)
    outro_local_realizacao_testagem = Column(String(100))
    
    # Vacina
    codigo_recebeu_vacina = Column(Float)
    codigo_laboratorio_primeira_dose = Column(String(100))
    codigo_laboratorio_segunda_dose = Column(String(100))
    lote_primeira_dose = Column(String(20))
    lote_segunda_dose = Column(String(20))
    codigo_doses_vacina = Column(String(20))
    data_primeira_dose = Column(Date)
    data_segunda_dose = Column(Date)
    
    # Comunidade
    codigo_contem_comunidade_tradicional = Column(Float)
    
    # Datas
    data_notificacao = Column(Date)
    data_inicio_sintomas = Column(Date)
    data_encerramento = Column(Date)
    
    # Testes
    total_testes_realizados = Column(Integer)
    
    # Teste 1
    codigo_estado_teste_1 = Column(SmallInteger)
    codigo_tipo_teste_1 = Column(SmallInteger)
    codigo_fabricante_teste_1 = Column(Integer)
    codigo_resultado_teste_1 = Column(SmallInteger)
    data_coleta_teste_1 = Column(Date)
    
    # Teste 2
    codigo_estado_teste_2 = Column(SmallInteger)
    codigo_tipo_teste_2 = Column(SmallInteger)
    codigo_fabricante_teste_2 = Column(Integer)
    codigo_resultado_teste_2 = Column(SmallInteger)
    data_coleta_teste_2 = Column(Date)
    
    # Teste 3
    codigo_estado_teste_3 = Column(SmallInteger)
    codigo_tipo_teste_3 = Column(SmallInteger)
    codigo_fabricante_teste_3 = Column(Integer)
    codigo_resultado_teste_3 = Column(SmallInteger)
    data_coleta_teste_3 = Column(Date)
    
    # Teste 4
    codigo_estado_teste_4 = Column(SmallInteger)
    codigo_tipo_teste_4 = Column(SmallInteger)
    codigo_fabricante_teste_4 = Column(Integer)
    codigo_resultado_teste_4 = Column(SmallInteger)
    data_coleta_teste_4 = Column(Date)
