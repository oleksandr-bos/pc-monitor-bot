from datetime import datetime

from pydantic import BaseModel, Field

class MetricPayload(BaseModel):
    cpu_percent: float = Field(..., ge=0, le=100, description="Загрузка CPU в процентах")
    ram_percent: float = Field(..., ge=0, le=100, description="Загрузка RAM в процентах")
    disk_percent: float | None = Field(None, ge=0, le=100, description="Загрузка диска в процентах")
    timestamp: datetime = Field(..., description="Момент снятия метрики на агенте, UTC")