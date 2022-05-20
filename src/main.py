from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello_world():
    json = request.get_json()
    user_price = float(json["resume"]["price"])
    vacancies = json["vacancies"]
    result = []
    for vacancie in vacancies:
        coef = float(vacancie["price"])/user_price
        result.append({"id": vacancie["id"], "score": coef if 0.8 <= coef <= 1.2 else 0})
    print(result, flush=True)
    return jsonify(result)

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
