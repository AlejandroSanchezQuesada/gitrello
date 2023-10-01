from flask import jsonify
from database.database import db
from database.database import Board 

# Variable to save the latest webhook
last_webhook = None


def process_json(data):
    global last_webhook
    last_webhook = data;
    
    new_board = Board(id_list=data['action']['data']['list']['id'],
                      name_list=data['action']['data']['list']['name'],
                      id_card=data['action']['data']['card']['id'],
                      name_card=data['action']['data']['card']['name'],
                      desc_card=data['action']['data']['card']['desc'])
    
    insert_or_update_board_data(new_board)
    
    return jsonify({"message": "Webhook recibido correctamente"})


def get_latest_webhook():
    if last_webhook is None:
        return jsonify({"message": "No se ha recibido ningún webhook aún"})
    return jsonify(last_webhook)


def insert_or_update_board_data(board):
 
    if(check_if_record_exists(board.id_card)):
        print("Ejecutando modificación de datos")
        update_board_data(board.id_card, board.id_list,board.name_list, board.name_card,board.desc_card )
    else:
        print("Ejecutando creación tablero")
        create_board_data(board)
    
    return True



def check_if_record_exists(id_to_check):
    # Use query.get(id) to find the record by its primary key (id)
    record = Board.query.get(id_to_check)
    return record is not None 

def create_board_data(new_board):
    db.session.add(new_board)
    db.session.commit()
    
def update_board_data(id_to_update, new_id_list, new_name_list,new_name_card, new_desc_card):
    # Check if the board with the specified ID exists
    existing_board = Board.query.get(id_to_update)
    
    if existing_board:
        # Update the attributes of the existing board with the new data
        existing_board.id_list = new_id_list
        existing_board.name_list = new_name_list
        existing_board.name_card = new_name_card
        existing_board.desc_card = new_desc_card

        # Commit the changes to the database
        db.session.commit()
        print(f"Tarjeta del tablero {new_name_list} actualizada con éxito")
    else:
        return print(f"La actualización de datos ha fallado")