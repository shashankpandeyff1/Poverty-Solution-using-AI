from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load the trained AI model
model = joblib.load("model/job_recommender_model.pkl")

# Simulated services data by location
services_data = {
    "Delhi": ["Govt. Skill Centre - Karol Bagh", "Digital Job Camp - July 25"],
    "Mumbai": ["NGO Job Helpdesk - Dharavi", "Resume Workshop - Andheri"],
    "Rural": ["Mobile Van Training Program", "PMKVY Registration Drive"]
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    skill_input = request.form['skill']
    location = request.form['location']

    # Predict job role
    predicted_job = model.predict([skill_input])[0]

    # Match local services
    services = services_data.get(location, ["Local Panchayat Help Center", "Call 1098 for support"])

    return render_template("index.html", name=name, predicted_job=predicted_job, services=services)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
