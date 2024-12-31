import os
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")  
def home():
    return render_template("index.html")

exercises_db= {
    "cardio": ["Running", "Cycling", "Jumping Jacks", "Burpees", "Mountain Climbers"],
    "strength": ["Push-ups", "Squats", "Lunges", "Plank", "Deadlifts"],
    "flexibility": ["Yoga", "Hamstring Stretch", "Hip Flexor Stretch", "Cobra Stretch", "Quad Stretch"],
}

@app.route("/workout.generator", methods=["POST"])
def workout_generator():
    data = request.get_json()
    workout_type = data.get("workout_type")
    duration = data.get("duration")
    print (data, workout_type, duration)

    if workout_type not in exercises_db:
        return jsonify({"error": "Invalid workout type. Choose cardio, strength, or flexibility."}), 400

    exercises = exercises_db[workout_type]
    workout_plan = random.sample(exercises, min(len(exercises), duration))
    return jsonify({"workout_plan": workout_plan})
    

if __name__ == "__main__":
    # Use the PORT environment variable provided by Render or default to 5000
    port = int(os.environ.get("PORT", 1000))
    app.run(host="0.0.0.0", port=port)
