from flask import Flask, request, render_template
import joblib
import numpy as np


app = Flask(__name__)

model  = joblib.load('Prediction_Model')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        price = request.form['price']
        kms = request.form['kms']
        fuel = request.form['fuel']
        seller = request.form['seller']
        mode = request.form['mode']





if __name__ == "__main__":
    app.run(debug=True)