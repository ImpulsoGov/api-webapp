from app.models import db
Base = db.Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,String,Boolean,TIMESTAMP,ForeignKey


class UsuarioSM(Base):
    __tablename__ = 'usuarios_sm'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,comment='Chave de Identificação Unica')   
    municipio_id_ibge = Column(String,nullable=False,comment='Municipio de atuação do usuario')
    cargo = Column(String,nullable=False,comment='Cargo atuação do usuario')
    telefone = Column(String,nullable=False,comment='Telefone de contato')
    whatsapp = Column(Boolean,nullable=False, comment='Numero informado possui whatsapp')
    id_usuario = Column(UUID(as_uuid=True),ForeignKey("suporte.usuarios.id"),nullable=False, default=uuid.uuid4,comment='Perfil de Acesso ID')
    unidade_saude = Column(String,nullable=False,comment='unidade de atuação do usuario')
    criacao_data = Column(TIMESTAMP,nullable=False,comment='Data de Criação')
    atualizacao_data = Column(TIMESTAMP,nullable=False,comment='Data de Atualização')
    __table_args__ = {'schema': 'suporte'}