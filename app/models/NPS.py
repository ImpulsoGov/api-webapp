from sqlalchemy import Column,DATE,Integer, ForeignKey
from app.models import db
from app.models.usuarios import Usuario
Base = db.Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class NPS(Base):
    __tablename__ = 'nps'
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("suporte.usuarios.id"),primary_key=True,  default=uuid.uuid4,comment='Chave de Identificação Unica do Usuario')   
    avaliacao = Column(Integer,comment='Avaliação')
    criacao_data = Column(DATE,nullable=False,comment='Data de Criação')
    usuario = relationship(Usuario, backref="nps")
    __table_args__ = {'schema': 'impulso_previne'}