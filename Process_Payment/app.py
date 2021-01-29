from flask import Flask, jsonify, request
from config import FLASK_SERVER, FLASK_PORT, FLASK_LOGGING
from process_payment import Payment
import datetime, json
app = Flask(__name__)

def toDate(dateString):
    return datetime.datetime.strptime(dateString, "%Y-%m-%d").date()

@app.route("/api/v1/payments/", methods=["POST"])
def member_create():
    content = json.loads(request.json)
    credit_card_number = content["CreditCardNumber"]
    card_holder = content["CardHolder"]
    expiration_date = datetime.datetime.strptime(content["ExpirationDate"], "%Y-%m-%d %H:%M:%S.%f")
    security_code = content["SecurityCode"]
    amount = content["Amount"]
    pay = Payment()
    response = pay.process_payment(credit_card_number,card_holder,expiration_date,security_code,amount)
    return response


if __name__ == "__main__":
    app.run(host=FLASK_SERVER, port=FLASK_PORT, debug=False)