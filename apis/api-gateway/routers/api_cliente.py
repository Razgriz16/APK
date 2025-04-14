from fastapi import APIRouter, HTTPException, Query, Depends
from contextlib import asynccontextmanager
from nats.aio.client import Client as NATS
import asyncio
import json
import logging
from dtos.cliente_dto import LoginDto
from utils.nats import get_nats_connection

router = APIRouter(prefix="/api/v1/clientes", tags=["Clientes"])

# Logger
logger = logging.getLogger(__name__)

# Config de NATS desde variables de entorno
NATS_SERVERS = ["nats://nats-server:4222"]
CLIENT_LOGIN_QUEUE = "cliente_login_queue"
REC_CLIENTE_QUEUE = "cliente_reccliente_queue"

@router.post("/login")
async def login(request_data: LoginDto, nc: NATS = Depends(get_nats_connection)):
    """Endpoint para manejar el login de clientes"""
    try:
        logger.info(f"data : {request_data}")
        message = json.dumps({'rut': request_data.rut, 'clave': request_data.clave}).encode()
        logger.info(f"message : {message}")

        if nc is None or nc.is_closed:
            logger.error("No hay conexión con NATS")
            raise HTTPException(status_code=503, detail="No hay conexión con el servidor de mensajería")

        response = await nc.request(CLIENT_LOGIN_QUEUE, message, timeout=5)
        response_data = json.loads(response.data.decode())
        
        logger.info(f"res : {response}")
        logger.info(f"res_data : {response_data}")

        if not isinstance(response_data,dict) or 'response' not in response_data or 'status_code' not in response_data:
            logger.error(f"Respuesta inválida de NATS: {response_data}")
            raise HTTPException(status_code=500, detail="Respuesta inválida del servicio")

        status_code = response_data.get('status_code', 200)
        data= response_data["response"]
        return {"response":data, "status_code":status_code}

    except asyncio.TimeoutError:
        logger.error("Timeout al contactar el servicio NATS")
        raise HTTPException(status_code=504, detail="Tiempo de espera agotado al contactar el servicio")
    except Exception as e:
        logger.error(f"Error en login: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.get("/recuperar-cliente")
async def recuperar_cliente(rut: str = Query(..., description="Rut del cliente"), nc: NATS = Depends(get_nats_connection)):
    """Endpoint para recuperar información del cliente"""
    try:
        logger.info(f"data : {rut}")
        message = json.dumps({'rut': rut}).encode()

        if nc is None or nc.is_closed:
            logger.error("No hay conexión con NATS")
            raise HTTPException(status_code=503, detail="No hay conexión con el servidor de mensajería")

        response = await nc.request(REC_CLIENTE_QUEUE, message, timeout=5)
        response_data = json.loads(response.data.decode())

        if not isinstance(response_data,dict) or 'response' not in response_data or 'status_code' not in response_data:
            logger.error(f"Respuesta inválida de NATS: {response_data}")
            raise HTTPException(status_code=500, detail="Respuesta inválida del servicio")

        status_code = response_data.get('status_code', 200)
        data= response_data["response"]
        return {"response":data, "status_code":status_code}

    except asyncio.TimeoutError:
        logger.error("Timeout al contactar el servicio NATS")
        raise HTTPException(status_code=504, detail="Tiempo de espera agotado al contactar el servicio")
    except Exception as e:
        logger.error(f"Error en login: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
