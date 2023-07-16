from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def index():
    # Simulando a leitura da planilha de dados em formato JSON
    dados = [
        {"nome": "João", "idade": 25, "cidade": "São Paulo"},
        {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
        {"nome": "Pedro", "idade": 35, "cidade": "Belo Horizonte"}
    ]
    
    # Retornando os dados da planilha em formato JSON
    return jsonify(dados)

if __name__ == "__main__":
    app.run()

