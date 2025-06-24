# utils/nats_utils.py
from nats.aio.client import Client as NATS
import asyncio
import logging

logger = logging.getLogger(__name__)

NATS_SERVERS = ["nats://nats-server:4222"]

async def get_nats_connection():
    """Dependencia para obtener una conexión a NATS"""
    nc = NATS()
    try:
        await nc.connect(servers=NATS_SERVERS)
        logger.info(f"Conectado a NATS en {NATS_SERVERS}")
        yield nc
    finally:
        if not nc.is_closed:
            await nc.close()
            logger.info("Conexión a NATS cerrada")
