from app.models import db,indicadores_desempenho_score_equipes_validas
session = db.session
IndicadorDesempenho = indicadores_desempenho_score_equipes_validas.IndicadorDesempenho

from .response_pages.indicadores import html as response_indicadores
from fastapi.responses import HTMLResponse

def consulta_indicadores_desempenho(municipio_uf):
     if municipio_uf :
        return session.query(IndicadorDesempenho).filter_by(municipio_uf=municipio_uf).all()
     else: 
        return session.query(IndicadorDesempenho).all()