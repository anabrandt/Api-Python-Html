from flask import Flask, request
import db_carros
import traceback


app = Flask(__name__)

@app.route("/carros", methods=["POST"])
def get_all():
    try:
        dados = db_carros.recupera_carros()
        resposta = []
        for reg in dados:
            carro = {}
            carro ["id"] = reg[0]
            carro ["ano"] = reg[1]
            carro ["montadora"] = reg[2]
            carro ["modelo"] = reg[3]
            carro ["placa"] = reg[4]
            resposta.append(carro)

        return resposta, 200
    except Exception as erro:
        traceback.print_exc()
        info = {"msg": "Erro de sistema"}, 404


@app.route("/carros", methods=["POST"])
def insere_carro():
    try:
        dado = request.json
        db_carros.insert_carro(dado)
        return dado, 200
    except Exception as erro:
        traceback.print_exc()
        info = {"msg": "Erro de sistema"}
        return info, 406

app.run(debug=True)
