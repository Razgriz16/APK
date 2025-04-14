FROM python:3.9-slim

# Variables de entorno para la instalación de Oracle Instant Client
ENV ORACLE_CLIENT_VERSION=21.1.0.0.0
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_1
ENV ORACLE_HOME=/opt/oracle/instantclient_21_1
ENV TNS_ADMIN=/opt/oracle/network/admin

# Crear la carpeta para el archivo tnsnames.ora
RUN mkdir -p ${TNS_ADMIN}

# Copiar el archivo tnsnames.ora al contenedor
COPY ./oracle_config/tnsnames.ora ${TNS_ADMIN}/

# Instalación de dependencias necesarias
RUN apt-get update && \
    apt-get install -y \
    libaio1 wget unzip && \
    mkdir -p /opt/oracle && \
    wget https://download.oracle.com/otn_software/linux/instantclient/211000/instantclient-basic-linux.x64-21.1.0.0.0.zip && \
    unzip instantclient-basic-linux.x64-21.1.0.0.0.zip -d /opt/oracle && \
    rm instantclient-basic-linux.x64-21.1.0.0.0.zip && \
    cd /opt/oracle/instantclient_21_1 && \
    rm -f libclntsh.so libocci.so && \
    ln -s libclntsh.so.21.1 libclntsh.so && \
    ln -s libocci.so.21.1 libocci.so && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalar herramientas básicas de conectividad
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
    tcpdump



COPY requisitos.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requisitos.txt

# Instalar cx_Oracle (controlador de Python para Oracle) y Flask
RUN pip install cx_Oracle Flask

# Exponer el puerto 5000
EXPOSE 5000

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el código de la aplicación al contenedor
COPY . .

# Comando por defecto para ejecutar la aplicación
CMD ["python", "main.py"]
