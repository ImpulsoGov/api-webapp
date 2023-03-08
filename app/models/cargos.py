from app.models import db
Base = db.Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,String,TIMESTAMP


class Cargo(Base):
    __tablename__ = 'cargos'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,comment='Chave de identificação única')
    nome = Column(String,nullable=False,comment='Nome do cargo')
    __table_args__ = {'schema': 'suporte'}
    criacao_data = Column(TIMESTAMP,nullable=False,comment='Data de criação')
    atualizacao_data = Column(TIMESTAMP,nullable=False,comment='Data de atualização')
