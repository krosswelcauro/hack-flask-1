from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#hack 1
@app.route('/users', methods=['GET'])
def get_users():
    return {"payload": "success"}

#hack 2
@app.route('/user', methods=['POST'])
def create_user():
    return {"payload": "success"}

#hack 3
@app.route('/user', methods=['DELETE'])
def delete_user():
    return {"payload": "success"}

#hack 4
@app.route('/user', methods=['PUT'])
def update_user():
    return {"payload": "success", "error": False}

#hack 5
@app.route('/api/v1/users', methods=['GET'])
def get_users_api():
    return {"payload": []}

#hack 6
@app.route('/api/v1/user', methods=['POST'])
def store_user_api():
    email = request.args.get("email")
    name = request.args.get("name")
    return jsonify({"payload": {
        "email": email,
        "name": name
    }})
    
#hack 7
@app.route('/api/v1/user/add', methods=['POST'])
def add_user_api():
    email = request.form.get("email")
    name = request.form.get("name")
    id = request.form.get("id")
    return jsonify({"payload": {
        "email": email,
        "name": name,
        "id": id
    }})
    
#hack 8
@app.route('/api/v1/user/create', methods=['POST'])
def create_user_api():
    request_data = request.get_json()
    email = request_data["email"]
    name = request_data["name"]
    id = request_data["id"]

    return jsonify({"payload": {
        "email": email,
        "name": name,
        "id": id
    }})


if __name__ == "__main__":
    app.run(debug=True)