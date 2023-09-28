from flask import Flask, render_template, request
from mongo import MongoConnection

app = Flask(__name__)

# Configura la conexión a la base de datos
db_client = MongoConnection().client
db = db_client.get_database('airbnb')
col = db.get_collection('sites')

@app.route('/', methods=['GET'])
def index():
    site_name = request.args.get('site_name')

    if site_name:
        # Consulta los documentos en la colección 'sites'
        airbnb_data = col.find({'title': {'$regex': site_name, '$options': 'i'}})
    else:
        # Consulta todos los documentos en la colección 'sites'
        airbnb_data = col.find({})

    # Uso de una plantilla HTML para mostrar los datos
    return render_template('index.html', airbnb_data=airbnb_data)

if __name__ == '__main__':
    app.run(debug=True)