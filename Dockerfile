FROM python:3.13-slim

# Variables
ENV FIREBIRD_VERSION=4.0.3.2975-0

# Instala dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget \
    libtommath1 \
    libicu-dev \
    libncurses6 \
    libfbclient2 \
    && apt-get clean

# Descarga e instala el cliente Firebird 4.0
RUN wget https://github.com/FirebirdSQL/firebird/releases/download/v4.0.3/Firebird-4.0.3.2975-0.amd64.tar.gz \
    && mkdir -p /opt/firebird \
    && tar -xzf Firebird-${FIREBIRD_VERSION}.amd64.tar.gz -C /opt/firebird --strip-components=1 \
    && rm Firebird-${FIREBIRD_VERSION}.amd64.tar.gz

# Forzar uso del cliente correcto
RUN ln -sf /opt/firebird/lib/libfbclient.so.4 /usr/lib/libfbclient.so

# Agrega cliente Firebird a la librería del sistema
ENV LD_LIBRARY_PATH=/opt/firebird/lib:$LD_LIBRARY_PATH
ENV PATH=/opt/firebird/bin:$PATH

# Instala Python requirements
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]