from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("gold_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    year = int(request.form["year"])
    currency = request.form["currency"]

    pred = model.predict([[year]])[0]
    if currency == "USD":
        price =pred[0]
        symbol = "$"
    elif currency == "INR":
        price = pred[3]
        symbol = "₹"
    elif currency == "EUR":
        price = pred[1]
        symbol = "€"
    elif currency == "GBP":
        price = pred[2]
        symbol = "£"
    elif currency == "AED":
        price = pred[4]
        symbol = "د.إ"

    elif currency == "CNY":
        price = pred[5]
        symbol = "¥"

    else:
        price = pred
        symbol = "$"

    return render_template("index.html",
        prediction=f"Predicted gold price : {symbol} {round(price,2)}",year=year,currency=currency)

if __name__ == "__main__":
    app.run(debug=True)