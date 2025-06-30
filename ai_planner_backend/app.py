from flask import Flask, request, jsonify, render_template_string, send_from_directory
from main import get_ai_trip_plan
import os

# Point to root TRANSITARA directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(__name__)

@app.route('/')
def home():
    # Load HTML from parent folder
    html_path = os.path.join(BASE_DIR, "TripPlanner.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    return render_template_string(html)

@app.route('/plan_trip', methods=['POST'])
def plan_trip():
    if request.is_json:
        data = request.get_json()
        destination = data.get('destination')
        days = data.get('days')
        plan = get_ai_trip_plan(destination, days)
        return jsonify({'plan': plan})
    return jsonify({'plan': 'Invalid request'}), 400

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
