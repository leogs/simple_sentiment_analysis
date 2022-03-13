import os
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from dotenv import find_dotenv, load_dotenv

app = Flask(__name__)
load_dotenv(find_dotenv())

app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "?????"

@app.route('/predict_sentiment', methods=['POST'])
@basic_auth.required
def predict_sentiment():
    sentence = request.get_json()['sentence']
    tb = TextBlob(sentence).translate(to='en')
    polarity = tb.sentiment.polarity
    return jsonify({'polarity': polarity})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)