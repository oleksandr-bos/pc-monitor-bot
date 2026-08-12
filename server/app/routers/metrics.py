import logging 

from fastapi import APIRouter
from pcmonitor_shared.schemas import MetricPayload

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.post("/")
def receive_metric(payload: MetricPayload) -> MetricPayload:
    logger.info(
        "Получена метрика: cpu=%.1f%% ram=%.1f%% ts=%s",
        payload.cpu_percent,
        payload.ram_percent,
        payload.timestamp,
    )
    return payload