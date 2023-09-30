from flask import jsonify

# Variable para almacenar el último webhook recibido
last_webhook = None


def process_json(data):
    global last_webhook
    last_webhook = data;
    
    # Procesar el webhook recibido
    # Imprimir el webhook en la consola
    print("Nuevo webhook recibido")
    print(f"Nombre del tablero :{data['action']['data']['board']['name']}")
    print(f"id Lista del Tablero :{data['action']['data']['list']['id']}")
    print(f"Lista del tablero :{data['action']['data']['list']['name']}")
    print(f"Cambios o nueva tarjeta :{data['action']['data']['card']['id']} \n {data['action']['data']['card']['name']} \n  {data['action']['data']['card']['desc']} ")
    
    return jsonify({"message": "Webhook recibido correctamente"})


def get_latest_webhook():
    if last_webhook is None:
        return jsonify({"message": "No se ha recibido ningún webhook aún"})
    return jsonify(last_webhook)