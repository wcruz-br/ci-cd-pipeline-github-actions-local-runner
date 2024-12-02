# Use uma imagem base do Python
FROM python:3.12.0-slim

# Defina o diretório de trabalho
WORKDIR /

# Copie o arquivo de requisitos e instale as dependências
RUN mkdir -p /app
COPY ./app/requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copie os arquivos da aplicação
COPY ./app /app

# Exponha a porta que o Gunicorn usará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "app.wsgi:app"]
