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
