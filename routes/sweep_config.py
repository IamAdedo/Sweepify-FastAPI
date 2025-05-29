from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.session import get_db
from app.models import SweepConfig
from app.schemas.sweep_config import SweepConfigCreate, SweepConfigResponse
from app.routes.user import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/sweep/config", response_model=SweepConfigResponse)
async def create_sweep_config(
    config: SweepConfigCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sweep = SweepConfig(
        user_id=current_user.id,
        blockchain=config.blockchain,
        source_wallet=config.source_wallet,
        destination_wallet=config.destination_wallet,
        enabled=config.enabled,
        min_balance=config.min_balance,
    )
    db.add(sweep)
    await db.commit()
    await db.refresh(sweep)
    return sweep
