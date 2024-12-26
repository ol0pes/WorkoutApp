from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define workout options
workouts = {
    "cardio": ["Running", "Jumping Jacks", "Burpees", "Cycling", "Rowing"],
    "strength": ["Push-ups", "Squats", "Deadlifts", "Bench Press", "Pull-ups"],
    "flexibility": ["Yoga", "Stretching", "Pilates", "Tai Chi", "Foam Rolling"]
}

@app.route('/generate_workout', methods=['POST'])
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
    app.run(debug=True)
