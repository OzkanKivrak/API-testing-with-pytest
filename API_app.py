from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ozkan"},
    {"id": 2, "name": "Ali"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    # VALIDATION
    if not data or "name" not in data or not data["name"]:
        return jsonify({
            "error": "name field is required"
        }), 400

    users.append({
        "id": len(users) + 1,
        "name": data["name"]
    })

    return jsonify({
        "message": "user created"
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
