from flask import Flask, render_template, url_for, request, jsonify
import random
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl.compressed')



@app.route('/')
def index():
    return render_template('base.html')

@app.route('/get_result', methods=['POST'])
def result():
    if request.method == 'POST':
        data = request.json
        res = model.predict([data['Sentence']])
       
        if res == -1:
            return jsonify('negative')
        if res == 0:
            return jsonify('neutral')
        else:
            return jsonify('positive')

if __name__ == "__main__":
    app.run(debug=True)