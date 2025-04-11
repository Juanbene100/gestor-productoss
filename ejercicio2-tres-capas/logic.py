from data import guardar_producto, listar_productos

contador_id = 1

def agregar_producto(data):
    global contador_id

    if not data or 'nombre' not in data:
        return {'mensaje': {'error': 'Falta el nombre del producto'}, 'status': 400}

    producto = {
        'id': contador_id,
        'nombre': data['nombre']
    }

    guardar_producto(producto)
    contador_id += 1

    return {'mensaje': {'mensaje': 'Producto agregado exitosamente', 'producto': producto}, 'status': 201}

def obtener_productos():
    return listar_productos()
