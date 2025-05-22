from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Mot de passe en dur
PASSWORD = "indigenas"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check-password", methods=["POST"])
def check_password():
    data = request.get_json()
    user_input = data.get("password", "")
    if user_input == PASSWORD:
        return jsonify({"result": "isso ae"})
    elif user_input == "Pedro Alvares Cabral":
        return jsonify({"result": "MANO NAO. SO NAO."})
    else:
        return jsonify({"result": "nuh uh"})

if __name__ == "__main__":
    app.run(debug=True)
