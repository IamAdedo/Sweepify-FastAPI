from sqlalchemy import Column, String, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum

from app.db.base_class import Base

class Blockchain(str, enum.Enum):
    PI = "pi"
    BTC = "btc"
    ETH = "eth"
    TON = "ton"
    SUI = "sui"

class SweepConfig(Base):
    __tablename__ = "sweep_configs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))

    blockchain = Column(Enum(Blockchain), nullable=False)
    source_wallet = Column(String, nullable=False)
    destination_wallet = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)
    min_balance = Column(Float, default=0.0)

    user = relationship("User", back_populates="sweep_configs")
