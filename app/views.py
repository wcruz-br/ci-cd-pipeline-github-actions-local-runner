from datetime import datetime
from flask import Blueprint, current_app

views = Blueprint('views', __name__)

@views.route("/")
def home():

    # Obtem quantidade de visitas
    quantidade_de_visitas = current_app.db.visitas.count_documents({})

    # Monta tabela de visitas, lendo a coleção visitas por ordem de timestamp
    tabela_de_visitas = "<table><tr><th>Registro de visitas</th></tr>"
    cursor = current_app.db.visitas.find({}, {'_id': 0}).sort([('timestamp',-1)])
    for documento in cursor:
        tabela_de_visitas += f"<tr><td>{documento['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}</td></tr>"
    tabela_de_visitas += "</table>"

    # Monta resposta (antes de inserir no banco, assim só lista os outros)
    resposta =  "<h2>Olá, pessoa!</h2><br/>" \
                f"<p>Você é o visitante {quantidade_de_visitas + 1} dessa biboca</p><br/>" \
                "<p>Veja quando foram as visitas anteriores:</p><br/><br/>" \
                f"{tabela_de_visitas}"

    # Cria o índice da coleção se ele não existir
    index_info = current_app.db.visitas.index_information()
    if "timestamp_1" not in index_info:
        # Cria o índice se não existir
        current_app.db.visitas.create_index([("timestamp", -1)], name="timestamp_idx")

    # Insere um documento na coleção 'visitas'
    current_app.db.visitas.insert_one({
        "timestamp": datetime.now()
    })

    # Retorna a resposta
    return resposta
