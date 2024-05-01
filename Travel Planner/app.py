from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan_trip():
    user_preferences = request.json  # User preferences sent from frontend

    # Extract user preferences
    destination = user_preferences.get('destination')
    budget = user_preferences.get('budget')
    startDate = user_preferences.get('startDate')
    numDays = user_preferences.get('numDays')
    interest = user_preferences.get('Interest') 

    # Placeholder trip plan data (can be replace with actual data, in larger scales)
    trip_plan = {
        'destination': destination,
        'accommodations': ['Hotel A', 'Hotel B'],
        'activities': [interest, 'Hiking'],
        'itinerary': ['Day 1: Visit attractions\nDay 2: Explore',interest]
    }

    return jsonify(trip_plan)

if __name__ == '__main__':
    app.run(debug=True)
