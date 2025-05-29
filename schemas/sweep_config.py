from pydantic import BaseModel
from uuid import UUID
from enum import Enum

class Blockchain(str, Enum):
    PI = "pi"
    BTC = "btc"
    ETH = "eth"
    TON = "ton"
    SUI = "sui"

class SweepConfigCreate(BaseModel):
    blockchain: Blockchain
    source_wallet: str
    destination_wallet: str
    enabled: bool = True
    min_balance: float = 0.0

class SweepConfigResponse(SweepConfigCreate):
    id: UUID
    user_id: UUID

    class Config:
        orm_mode = True
