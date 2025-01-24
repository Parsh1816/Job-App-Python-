# Project Structure:
# job_listing_app/
#   ├── app.py
#   ├── README.md
#   ├── static/
#   │   └── styles.css
#   ├── templates/
#   │   ├── index.html
#   │   └── details.html
#   └── jobs.json

# app.py
from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load jobs from JSON file
def load_jobs():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jobs_path = os.path.join(current_dir, 'jobs.json')
    with open(jobs_path, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    jobs = load_jobs()
    job = next((job for job in jobs if job['id'] == job_id), None)
    
    if job:
        return render_template('details.html', job=job)
    else:
        return jsonify({"error": "Job not found"}), 404

@app.route('/api/jobs')
def get_all_jobs():
    jobs = load_jobs()
    return jsonify(jobs)

@app.route('/api/job/<int:job_id>')
def get_job_by_id(job_id):
    jobs = load_jobs()
    job = next((job for job in jobs if job['id'] == job_id), None)
    
    if job:
        return jsonify(job)
    else:
        return jsonify({"error": "Job not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
