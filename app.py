from flask import Flask, request, jsonify
import random
import os


app = Flask(__name__)

# Define workout options
workouts = {
    "cardio": ["Running", "Jumping Jacks", "Burpees", "Cycling", "Rowing"],
    "strength": ["Push-ups", "Squats", "Deadlifts", "Bench Press", "Pull-ups"],
    "flexibility": ["Yoga", "Stretching", "Pilates", "Tai Chi", "Foam Rolling"]
}


@app.route("/Generate workout")
def generate_workout():
    data = request.json
    workout_type = data.get('workout_type')
    duration = data.get('duration')

    if workout_type not in workouts:
        return jsonify({"error": "Invalid workout type. Choose cardio, strength, or flexibility."}), 400

    try:
        duration = int(duration)
        exercises = workouts[workout_type]
        workout_plan = random.sample(exercises, min(len(exercises), duration))
        return jsonify({"workout_plan": workout_plan})
    except ValueError:
        return jsonify({"error": "Invalid duration. Please provide a number."}), 400

if __name__ == '__main__':
    # Get the PORT from the environment or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
