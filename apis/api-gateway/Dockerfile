# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Instalar herramientas básicas de conectividad (opcional)
RUN apt-get update && apt-get install -y \
    curl \
    iputils-ping \
    dnsutils \
    netcat-openbsd \
    telnet \
    wget \
    iproute2 \
    net-tools \
    traceroute \
    tcpdump && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requisitos.txt .
COPY config/ ./config/
COPY dtos/ ./dtos/
COPY routers/ ./routers/
COPY utils/ ./utils/
COPY app.py .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requisitos.txt

# Exponer el puerto donde el API Gateway escuchará
EXPOSE 8001

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
