from flask import Flask, render_template, jsonify

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.route('/')
def index():
    return 'This Is Working!'

@app.route('/json')
def location():
    return jsonify(name="Starbucks", address=8)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)