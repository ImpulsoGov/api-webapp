from sqlalchemy import Column,DATE,Integer, ForeignKey
from app.models import db
from app.models.usuarios import usuarios
from app.models import db
Base = db.Base_impulso_previne_nominal
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class NPS(Base):
    __tablename__ = 'nps'
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("suporte.usuarios.id"),primary_key=True,  default=uuid.uuid4,comment='Chave de Identificação Unica do Usuario')   
    avaliacao = Column(Integer,comment='Avaliação')
    criacao_data = Column(DATE,nullable=False,comment='Data de Criação')
    __table_args__ = {'schema': 'impulso_previne'}