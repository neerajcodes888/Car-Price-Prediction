from flask import Flask, request, render_template
import joblib
import numpy as np
import datetime

app = Flask(__name__)

model  = joblib.load('Prediction_Model')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        price = float(request.form['price'])
        kms = float(request.form['kms'])
        fuel = request.form['fuel']
        seller = request.form['seller']
        mode = request.form['mode']
        own = request.form['own']
        year = request.form['year']
        




if __name__ == "__main__":
    app.run(debug=True)