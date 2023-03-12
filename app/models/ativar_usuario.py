from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from app.models import db

Base = db.Base
import uuid


class Ativar(Base):
    __tablename__ = "ativar_usuario"
    usuario_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment="Usuário ID",
    )
    codigo_ativacao = Column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        comment="Codigo de Ativação do Usuário",
    )
    __table_args__ = {"schema": "suporte"}


# Base.metadata.create_all(db.engine)
