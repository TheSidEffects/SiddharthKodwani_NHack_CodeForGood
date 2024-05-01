from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/places')
def get_places():
    # You can load data from a JSON file or a database
    # For simplicity, let's assume data is stored in a JSON file
    with open('data/places.json') as f:
        places = json.load(f)
    return jsonify(places)

if __name__ == '__main__':
    app.run(debug=True)
