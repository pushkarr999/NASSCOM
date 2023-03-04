import numpy as np
from flask import Flask, request, render_template
import pickle
from datetime import date
from flask import Markup

app = Flask(__name__)

model_Adilabad = pickle.load(open('models/model_Adilabad.pkl', 'rb'))
model_Karimnagar = pickle.load(open('models/model_Karimnagar.pkl', 'rb'))
model_Khammam = pickle.load(open('models/model_Khammam.pkl', 'rb'))
model_Nizamabad = pickle.load(open('models/model_Nizamabad.pkl', 'rb'))
model_Warangal = pickle.load(open('models/model_Warangal.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    if features[0] == "Adilabad":
        # features = [np.array(features)]
        # prediction = model.predict(features)
        predictions = model_Adilabad.predict(start=84, end=84 + int(features[1]) - 1, typ='levels').rename(
            'Predictions')
        ans = "<p align='center'>" + str(features[0]) +"</p><br>"+"<table align='center' class='table'><tr><th scope='col'>Date</th><th scope='col'>AQI</th></tr>"
        for i in range(len(predictions)):
            ans += "<tr><td>" + str(date.strftime(predictions.index[i], '%b-%y')) + "</td><td>" + str(int(predictions[i])) + "</td></tr>"
        ans += "</table>"
        result = Markup(ans)
    elif features[0] == "Karimnagar":
        # features = [np.array(features)]
        # prediction = model.predict(features)
        predictions = model_Karimnagar.predict(start=84, end=84 + int(features[1]) - 1, typ='levels').rename(
            'Predictions')
        ans = "<p align='center'>" + str(features[0]) +"</p><br>"+"<table align='center' class='table'><tr><th scope='col'>Date</th><th scope='col'>AQI</th></tr>"
        for i in range(len(predictions)):
            ans += "<tr><td>" + str(date.strftime(predictions.index[i], '%b-%y')) + "</td><td>" + str(int(predictions[i])) + "</td></tr>"
        ans += "</table>"
        result = Markup(ans)
    elif features[0] == "Khammam":
        # features = [np.array(features)]
        # prediction = model.predict(features)
        predictions = model_Khammam.predict(start=84, end=84 + int(features[1]) - 1, typ='levels').rename(
            'Predictions')
        ans = "<p align='center'>" + str(features[0]) +"</p><br>"+"<table align='center' class='table'><tr><th scope='col'>Date</th><th scope='col'>AQI</th></tr>"
        for i in range(len(predictions)):
            ans += "<tr><td>" + str(date.strftime(predictions.index[i], '%b-%y')) + "</td><td>" + str(int(predictions[i])) + "</td></tr>"
        ans += "</table>"
        result = Markup(ans)
    elif features[0] == "Nizamabad":
        # features = [np.array(features)]
        # prediction = model.predict(features)
        predictions = model_Nizamabad.predict(start=84, end=84 + int(features[1]) - 1, typ='levels').rename(
            'Predictions')
        ans = "<p align='center'>" + str(features[0]) +"</p><br>"+"<table align='center' class='table'><tr><th scope='col'>Date</th><th scope='col'>AQI</th></tr>"
        for i in range(len(predictions)):
            ans += "<tr><td>" + str(date.strftime(predictions.index[i], '%b-%y')) + "</td><td>" + str(int(predictions[i])) + "</td></tr>"
        ans += "</table>"
        result = Markup(ans)
    elif features[0] == "Warangal":
        # features = [np.array(features)]
        # prediction = model.predict(features)
        predictions = model_Warangal.predict(start=84, end=84 + int(features[1]) - 1, typ='levels').rename(
            'Predictions')
        ans = "<p align='center'>" + str(features[0]) +"</p><br>"+"<table align='center' class='table'><tr><th " \
                                                                  "scope='col'>Date</th><th scope='col'>AQI</th></tr> "
        for i in range(len(predictions)):
            ans += "<tr><td>" + str(date.strftime(predictions.index[i], '%b-%y')) + "</td><td>" + str(int(predictions[i])) + "</td></tr>"
        ans += "</table>"
        result = Markup(ans)

    return render_template('index.html', prediction=result)



if __name__ == "__main__":
    app.run(debug=True)
