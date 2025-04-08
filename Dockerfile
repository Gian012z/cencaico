FROM python:3.11-slim

# Instala Firebird client
RUN apt-get update && apt-get install -y firebird-dev libfbclient2 && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
