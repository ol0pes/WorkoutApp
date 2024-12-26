import os
from flask import Flask

app = Flask(__name__)

@app.route("/")  # Define the root route
def home():
    return "Welcome to the Workout Generator App!"

if __name__ == "__main__":
    # Use the PORT environment variable provided by Render or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


"""
class workout():{
    data = request.json
    workout_type = data.get('workout_type')
    duration = data.get('duration')}

    if workout_type not in workouts:
        return jsonify({"error": "Invalid workout type. Choose cardio, strength, or flexibility."}), 400

    try:
        duration = int(duration)
        exercises = workouts[workout_type]
        workout_plan = random.sample(exercises, min(len(exercises), duration))
        return jsonify({"workout_plan": workout_plan})
    except ValueError:
        return jsonify({"error": "Invalid duration. Please provide a number."}), 400
}
"""
