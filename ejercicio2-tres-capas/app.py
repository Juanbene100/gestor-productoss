from flask import Flask, request, jsonify
from logic import agregar_producto, obtener_productos

app = Flask(__name__)

@app.route('/productos', methods=['POST'])
def route_agregar_producto():
    data = request.get_json()
    resultado = agregar_producto(data)
    return jsonify(resultado['mensaje']), resultado['status']

@app.route('/productos', methods=['GET'])
def route_listar_productos():
    return jsonify(obtener_productos()), 200

if __name__ == '__main__':
    app.run(debug=True)
