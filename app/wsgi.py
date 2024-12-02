from app import create_app

# Ponto de entrada para servidores WSGI, como Gunicorn.
# Cria uma instância da aplicação para que o servidor possa servir.

app = create_app()

if __name__ == "__main__":
    app.run()
