import numpy as np
from flask import Flask, request, jsonify, render_template
# import pickle
import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load the saved model
model = joblib.load(open("sentiment_model.pkl", "rb"))
# model = joblib.load('sentiment_model.pkl')

# Load the CountVectorizer used during training
vectorizer = joblib.load(open("count_vectorizer.pkl", "rb"))

# create a route that manages user request and does sentiment prediction


@app.route("/")
def Home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    # Retrieve form data
    rating = request.form.get('Rating')
    title = request.form.get('Title')
    review = request.form.get('Review')

    # data = request.get_json()
    # Combine features into a text for prediction
    text = f"{rating} {title} {review}"

    # text = data['text']
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)[0]
    return render_template("index.html", prediction_text="The sentiment analysis is {}".format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
