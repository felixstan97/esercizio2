from flask import Flask, jsonify
import requests 
import json

' -----------------------  VARIABILI - '
resto = [{'uno': 2,'tre': 'quattro'},{'uno': 6, 'tre': 'otto'} ]
res = [{'uno': 4,'tre': 'abishnow'}]
qui= 'hola'
b = [
        {
        "nome": "Luca",
        "cognome": "Rossi", 
        "eta": 25,
        "online": False,
        "interessi": ["calcio","nuoto","basket"],
        "macchina": None
        },
        {
        "nome": "Franco",
        "cognome": "Vizzio", 
        "eta": 19,
        "online": True,
        "interessi": ["pallavolo","skteboard","sci"],
        "macchina": None
        }
    ]

' ------------------------ COSE - '
app = Flask(__name__)

@app.route('/')
def index():
    ris = jsonify(b)
    
    rar = aggiungiHeader(ris)
    return ris


@app.route("/je", methods=['GET'])	
def getje():
    ris = jsonify(resto)
    ris.headers.add("Access-Control-Allow-Origin", "*")
    return ris



@app.route("/jo", methods=['GET'])
def getJo():
    risposta_finale = jsonify(b)
    risposta_finale.headers.add("Access-Control-Allow-Origin", "*")
    return risposta_finale
    
def aggiungiHeader(corpo):
    return corpo.headers.add("Access-Control-Allow-Origin", "*")

' ------------------------ Cose che vanno alla fine - '
if __name__ == "__main__":
    app.run(debug=True)
''',host='0.0.0.0', port=4200'''

app.use(cors())
