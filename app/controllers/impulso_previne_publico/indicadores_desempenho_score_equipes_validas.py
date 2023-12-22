from app.models.impulso_previne_publico import indicadores_desempenho_score_equipes_validas
from app.models import db
session = db.session
IndicadoresDesempenho = indicadores_desempenho_score_equipes_validas.IndicadoresDesempenho

def consultar_indicadores_desempenho(municipio_uf):
   try: 
        return session.query(IndicadoresDesempenho).filter_by(municipio_uf=municipio_uf).with_entities(
               IndicadoresDesempenho.municipio_nome,
               IndicadoresDesempenho.municipio_uf,
               IndicadoresDesempenho.periodo_codigo,
               IndicadoresDesempenho.periodo_data_inicio,
               IndicadoresDesempenho.periodo_data_fim,
               IndicadoresDesempenho.indicador_ordem,
               IndicadoresDesempenho.indicador_prioridade,
               IndicadoresDesempenho.indicador_nome,
               IndicadoresDesempenho.indicador_peso,
               IndicadoresDesempenho.indicador_validade_resultado,
               IndicadoresDesempenho.indicador_acoes_por_usuario,
               IndicadoresDesempenho.indicador_numerador,
               IndicadoresDesempenho.indicador_denominador_estimado,
               IndicadoresDesempenho.indicador_denominador_utilizado_informado,
               IndicadoresDesempenho.indicador_denominador_utilizado,
               IndicadoresDesempenho.indicador_denominador_utilizado_tipo,
               IndicadoresDesempenho.indicador_denominador_informado_diferenca_utilizado,
               IndicadoresDesempenho.indicador_denominador_informado_diferenca_utilizado_formatado,
               IndicadoresDesempenho.indicador_nota,
               IndicadoresDesempenho.indicador_nota_porcentagem,
               IndicadoresDesempenho.indicador_meta,
               IndicadoresDesempenho.indicador_diferenca_meta,
               IndicadoresDesempenho.indicador_recomendacao,
               IndicadoresDesempenho.delta,
               IndicadoresDesempenho.delta_formatado,
               IndicadoresDesempenho.indicador_usuarios_100_porcento_meta,
               IndicadoresDesempenho.indicador_usuarios_cadastrados_sem_atendimento,
               IndicadoresDesempenho.indicador_usuarios_cadastrar_para_meta,
               IndicadoresDesempenho.indicador_score,
               IndicadoresDesempenho.indicador_denominador_informado
            ).all()
   except Exception as error:
        session.rollback()
        print({"erros" : [error]})
        return error