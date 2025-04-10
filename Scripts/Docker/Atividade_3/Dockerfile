# Dockerfile para ambiente ETL com Python + PostgreSQL + SQLAlchemy:
FROM python:3.10-slim

# Instalar dependencias do sistema:
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/liv/apt/lists/*

# Definir diretorios de trabalho:
WORKDIR /app

# Copiar arqivos do projeto:
COPY requirements.txt ./
COPY srag_2021.csv ./

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar arquivos do projeto
COPY etl_srag.py ./

# Comando padrão
CMD [ "python", "etl_srag.py"]