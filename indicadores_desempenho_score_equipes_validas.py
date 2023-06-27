from app.models import db,indicadores_desempenho_score_equipes_validas
session = db.session
IndicadorDesempenho = indicadores_desempenho_score_equipes_validas.IndicadorDesempenho

from .response_pages.indicadores import html as response_indicadores
from fastapi.responses import HTMLResponse

def consulta_indicadores_desempenho(id_sus,municipio_nome,municipio_uf,periodo_codigo, indicador_nome,indicador_meta,indicador_diferenca_meta, indicador_resultado):
    if estado_sigla != None : estado_sigla=estado_sigla.upper()
    params = {
        "municipio_id_sus":id_sus,
        "municipio_nome":municipio_nome,
        "municipio_uf":municipio_uf,
        "periodo_codigo": periodo_codigo,
        "indicador_nome":indicador_nome,
        "indicador_meta" : indicador_meta,
        "indicador_diferenca_meta": indicador_diferenca_meta,
        "indicador_validade_resultado":indicador_resultado
    
    }
    params = {coluna:parametro for coluna, parametro in params.items() if parametro!=None}
    if len(params)==0: 
        return session.query(IndicadorDesempenho).all()
    else:
        return session.query(IndicadorDesempenho).filter_by(**params).all()