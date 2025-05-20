import pandas as pd
from transform.data_cleaner import GenericCleaner

class Pipeline_transform_disease_table(GenericCleaner):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe
        self.column_mappings = {
    'source_id': 'source_id',
    'sexo': 'sexo',
    'racaCor': 'raca_cor',
    'idade': 'idade',
    'estado':'estado',
    'municipio':'municipio',
    'municipioNotificacao':'municipio_notificacao',
    'estadoNotificacao': 'estado_notificacao',
    'estadoNotificacaoIBGE':'estado_notificacao_IBGE',
    'sintomas': 'sintomas',
    'outrosSintomas': 'outros_sintomas',
    'condicoes': 'condicoes',
    'outrasCondicoes': 'outras_condicoes',
    'profissionalSaude': 'profissional_saude',
    'profissionalSeguranca': 'profissional_seguranca',
    'cbo': 'cbo',
    'evolucaoCaso': 'evolucao_caso',
    'classificacaoFinal': 'classificacao_final',
    'codigoEstrategiaCovid': 'codigo_estrategia_covid',
    'codigoBuscaAtivaAssintomatico': 'codigo_busca_ativa_assintomatico',
    'outroBuscaAtivaAssintomatico': 'outro_busca_ativa_assintomatico',
    'codigoTriagemPopulacaoEspecifica': 'codigo_triagem_populacao_especifica',
    'outroTriagemPopulacaoEspecifica': 'outro_triagem_populacao_especifica',
    'codigoLocalRealizacaoTestagem': 'codigo_local_realizacao_testagem',
    'outroLocalRealizacaoTestagem': 'outro_local_realizacao_testagem',
    'codigoRecebeuVacina': 'codigo_recebeu_vacina',
    'codigoLaboratorioPrimeiraDose': 'codigo_laboratorio_primeira_dose',
    'codigoLaboratorioSegundaDose': 'codigo_laboratorio_segunda_dose',
    'lotePrimeiraDose': 'lote_primeira_dose',
    'loteSegundaDose': 'lote_segunda_dose',
    'codigoDosesVacina': 'codigo_doses_vacina',
    'dataPrimeiraDose': 'data_primeira_dose',
    'dataSegundaDose': 'data_segunda_dose',
    'codigoContemComunidadeTradicional': 'codigo_contem_comunidade_tradicional',
    'dataNotificacao': 'data_notificacao',
    'dataInicioSintomas': 'data_inicio_sintomas',
    'dataEncerramento': 'data_encerramento',
    'totalTestesRealizados': 'total_testes_realizados',
    
    # Testes
    'codigoEstadoTeste1': 'codigo_estado_teste_1',
    'codigoTipoTeste1': 'codigo_tipo_teste_1',
    'codigoFabricanteTeste1': 'codigo_fabricante_teste_1',
    'codigoResultadoTeste1': 'codigo_resultado_teste_1',
    'codigoEstadoTeste2': 'codigo_estado_teste_2',
    'codigoTipoTeste2': 'codigo_tipo_teste_2',
    'codigoFabricanteTeste2': 'codigo_fabricante_teste_2',
    'codigoResultadoTeste2': 'codigo_resultado_teste_2',
    'codigoEstadoTeste3': 'codigo_estado_teste_3',
    'codigoTipoTeste3': 'codigo_tipo_teste_3',
    'codigoFabricanteTeste3': 'codigo_fabricante_teste_3',
    'codigoResultadoTeste3': 'codigo_resultado_teste_3',
    'codigoEstadoTeste4': 'codigo_estado_teste_4',
    'codigoTipoTeste4': 'codigo_tipo_teste_4',
    'codigoFabricanteTeste4': 'codigo_fabricante_teste_4',
    'codigoResultadoTeste4': 'codigo_resultado_teste_4',
    'dataColetaTeste1': 'data_coleta_teste_1',
    'dataColetaTeste2': 'data_coleta_teste_2',
    'dataColetaTeste3': 'data_coleta_teste_3',
    'dataColetaTeste4': 'data_coleta_teste_4',
}

    def _repeted_columns(self):
        '''Remoção das colunas que já constam na tabela município e que possuem dados nulos na tabela. 
        Para fins de exercicio vide questão 3.c II manterei a estadoNotificacaoIBGE.'''
        columns = ['municipioIBGE', 'municipioNotificacaoIBGE', 'estadoIBGE']
        self.df = self.column_remover(columns=columns)

    def _remove_same_value_columns(self):
        '''Remoção de colunas com valor único que não acrescentam à base.'''
        columns = ['excluido', 'validado', 'origem']
        self.df = self.column_remover(columns=columns)

    def _replace_null_value(self):
        '''Substituição dos valores nulos da coluna codigoRecebeuVacina por "3" (Ignorado, conforme o Dicionário de Dados do SUS).'''
        column = ['codigoRecebeuVacina']
        self.df = self.null_cleaner(column=column, filler='3')

    def _replace_data_for_boolean(self):
        '''Alteração do tipo de dado das colunas profissionalSeguranca e profissionalSaude para Boolean'''
        columns = ['profissionalSeguranca','profissionalSaude']
        for column in columns:
            self.change_data_from_rows(column=column, values={'Não':False,'Sim':True})
        
    def _rename_columns(self):
        """Padronizar o nome das colunas de acordo com a norma para o SQL"""
        for old_name, new_name in self.column_mappings.items():
            self.refactor_columns_name(old_name, new_name)

    def pipeline(self) -> pd.DataFrame:
        '''Execução da Pipeline'''
        self._repeted_columns()
        self._remove_same_value_columns()
        self._replace_null_value()
        self._replace_data_for_boolean()
        self._rename_columns()
        
        
        return self.df
    