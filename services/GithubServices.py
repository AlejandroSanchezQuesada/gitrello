import requests
from dotenv import load_dotenv
import os
from database.database import db
from database.database import Board 

load_dotenv()
github_token = os.getenv("GITHUB_TOKEN")
github_user = os.getenv("GITHUB_USER")
github_repository = os.getenv("GITHUB_REPOSITORY")

def create_issue(new_issue):
    if(check_issue_exists(new_issue.id_issue)):
        print("Existe luego se actualiza")
        update_issue(new_issue) 
    else:
        # Define los datos del issue
        issue_data = {
            "title": new_issue.name_card,
            "body": new_issue.desc_card,
        }

        # Configura la autenticación con tu token de acceso personal
        headers = {
            "Authorization": f"token {github_token}",  
        }

        # URL de la API para crear un issue en tu repositorio
        repo_owner = github_user
        repo_name = github_repository
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

        # Realiza la solicitud POST para crear el issue
        response = requests.post(url, json=issue_data, headers=headers)
        #print(jsonify(response.json.data["number"]))
    

        # Verifica si la solicitud fue exitosa
        if response.status_code == 201:
            #print(f"id de la issue {response.json()['number']}")
            print(f"id de la issue  {new_issue,response.json()['number']}")
            print(f"informacion de la issue  {new_issue}")
            set_issue_number(new_issue,response.json()['number'])
            print("Issue creado exitosamente.")
            print(f"URL del nuevo issue: {response.json()['html_url']}")
        else:
            print("No se pudo crear el issue. Código de estado:", response.status_code)
            print("Respuesta del servidor:", response.text)


def set_issue_number(update_board, idNumber):
    # Check if the board with the specified ID exists
    existing_board = Board.query.get(update_board.id_card)
    
    if existing_board:
        # Update the attributes of the existing board with the new data
        existing_board.id_issue = idNumber

        # Commit the changes to the database
        db.session.commit()
        print(f"Tarjeta del tablero asignada la issue correctamente")
    else:
        return print(f"La inserción de la issue en db ha fallado")
    
    
def check_issue_exists(id_issue_to_check):
    # Check if id_issue_to_check is None or empty
    if id_issue_to_check is None or id_issue_to_check == "":
        return False

    # Use the query method to check if a record with the given id_issue exists
    exists = db.session.query(Board).filter_by(id_issue=id_issue_to_check).scalar() is not None
    return exists

def update_issue(updated_issue):
    # Define the issue data to update
    issue_data = {
        "title": updated_issue.name_card,
        "body": updated_issue.desc_card,
    }

    # Construct the URL for the GitHub API to update the issue
    repo_owner = github_user
    repo_name = github_repository
    issue_number = updated_issue.id_issue
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}"

    # Configure the authentication with your personal access token
    headers = {
        "Authorization": f"token {github_token}",
    }

    # Make a PATCH request to update the issue
    response = requests.patch(url, json=issue_data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Issue {issue_number} actualizada exitosamente.")
        print(f"URL de la issue actualizada: {response.json()['html_url']}")
    else:
        print(f"No se pudo actualizar la issue {issue_number}. Código de estado: {response.status_code}")
        print("Respuesta del servidor:", response.text)