from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define workout options
#workouts = {
    #"cardio": ["Running", "Jumping Jacks", "Burpees", "Cycling", "Rowing"],
    #"strength": ["Push-ups", "Squats", "Deadlifts", "Bench Press", "Pull-ups"],
    #"flexibility": ["Yoga", "Stretching", "Pilates", "Tai Chi", "Foam Rolling"]
#}

@app.route("/Generate workout")
def home():
    return "Welcome to the Workout generator app"

if __name__ == '__main__':
    # Get the PORT from the environment or default to 5000
    import os
    port = int(os.environ.get("PORT", 1000))
    app.run(host="0.0.0.0", port=port)