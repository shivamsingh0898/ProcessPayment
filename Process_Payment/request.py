import requests
import datetime, json
date = datetime.datetime.now()
print(date)
# 2022-01-29 17:21:46.171848
obj = { "CreditCardNumber": "354673100235957",
        "CardHolder": 757,
        "ExpirationDate": datetime.datetime.strftime(date, "%Y-%m-%d %H:%M:%S.%f"),
        "SecurityCode": "CVV",
        "Amount": 100.7,
        }
# print(datetime.datetime.now())
r = requests.post('http://localhost:5000/api/v1/payments/', json=json.dumps(obj))
print(r.text)
