from flask import Flask, request, jsonify
from flask_cors import CORS
import qrcode

from algorand_utils import verify_transaction
from settlement import minimize_transactions

app = Flask(__name__)
CORS(app)

bills = {}
reputation = {}

@app.route("/create-bill", methods=["POST"])
def create_bill():
    data = request.json
    bill_id = data["bill_id"]

    bills[bill_id] = {
        "total": data["total"],
        "members": data["members"],
        "payments": {},
        "status": "pending"
    }
    return jsonify({"message": "Bill created"})


@app.route("/split", methods=["POST"])
def split():
    data = request.json
    bill = bills[data["bill_id"]]

    share = bill["total"] / len(bill["members"])

    for m in bill["members"]:
        bill["payments"][m] = {"due": share, "paid": False}

    return jsonify(bill)


@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    bill = bills[data["bill_id"]]

    if verify_transaction(data["txn_id"]):
        user = data["sender"]
        bill["payments"][user]["paid"] = True
        reputation[user] = reputation.get(user, 0) + 10

        return jsonify({"status": "verified"})

    return jsonify({"error": "invalid"}), 400


@app.route("/status/<bill_id>")
def status(bill_id):
    return jsonify(bills[bill_id])


@app.route("/settle/<bill_id>")
def settle(bill_id):
    return jsonify(minimize_transactions(bills[bill_id]))


@app.route("/reputation/<user>")
def rep(user):
    return jsonify({"score": reputation.get(user, 0)})


@app.route("/qr/<bill_id>")
def qr(bill_id):
    data = f"pay://bill={bill_id}&amount={bills[bill_id]['total']}"
    img = qrcode.make(data)
    file = f"{bill_id}.png"
    img.save(file)
    return jsonify({"qr": file})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)