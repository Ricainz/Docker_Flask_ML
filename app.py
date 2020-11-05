from flask import Flask, render_template, url_for, request, jsonify
import random

app = Flask(__name__)

def rand():
    result = random.sample([-1, 0, 1],  1)
    return result[0]

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/get_result', methods=['POST'])
def result():
    if request.method == 'POST':
        res = rand()
        if res == -1:
            return jsonify('negative')
        if res == 0:
            return jsonify('neutral')
        else:
            return jsonify('positive')

if __name__ == "__main__":
    app.run(debug=True)