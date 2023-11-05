from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask (__name__)

@app.route("/")
def index ():
    return "index"

@app.route ("/ping")
def ping():
    return jsonify({"message" : "Elizabeth"})

@app.route ("/usuarios/<string:nombre>")
def usuario_by_name (nombre):
    return jsonify ({"name": nombre})

@app.route ("/usuarios/<int:id>")
def usuario_by_id (id):
    return jsonify ({"name": id})

#GET DE TODOS LOS RESCURSOS
@app.route ("/recurso", methods = ["GET"])
def get_recursos():
    return jsonify({"data : todos los items del recurso"})

#POST NUEVO RECURSO
@app.route ("/recurso", methods = ["POST"])
def post_recursos():
    print (request.json())
    body = request.json
    name = body ["name"]
    modelo = body ["modelo"]
    
    return jsonify({"recurso" : {
                    "name" : name,
                    "modelo" : modelo
    }})
#GET un recurso
@app.route ("/recurso/<int:id>", methods = ["GET"])
def get_recurso_by_id (id):
     return jsonify({"recurso" : {
                    "name" : "name",
                    "modelo" : "modelo"
    }})




if __name__ == "__main__":

    app.run (debug=True, port= 5000)