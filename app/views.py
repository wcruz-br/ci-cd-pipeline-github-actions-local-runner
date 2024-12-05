from datetime import datetime
from flask import Blueprint, current_app

views = Blueprint('views', __name__)

@views.route("/")
def home():

    # Gets number of visits
    number_of_visits = current_app.db.visits.count_documents({})

    # Assembles visit table, reading the visit collection in reversed timestamp order
    visit_table = "<table><tr><th>Visit Log</th></tr>"
    cursor = current_app.db.visits.find({}, {'_id': 0}).sort([('timestamp',-1)])
    for document in cursor:
        visit_table += f"<tr><td>{document['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}</td></tr>"
    visit_table += "</table>"

    # Assembles the response (before inserting into the database, so it only lists the others)
    response =  "<h2>Hello, person!</h2><br/>" \
                f"<p>You are visitor {number_of_visits + 1} to this place</p><br/>" \
                "<p>See when the previous visits were here:</p><br/><br/>" \
                f"{visit_table}"

    # Creates the collection index if it doesn't exist
    index_info = current_app.db.visits.index_information()
    if "timestamp_1" not in index_info:
        current_app.db.visits.create_index([("timestamp", -1)], name="timestamp_idx")

    # Inserts a document into the 'visits' collection
    current_app.db.visits.insert_one({
        "timestamp": datetime.now()
    })

    # Returns the response
    return response
