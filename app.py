import os
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Kampala, Uganda',
        'salary': 'UGX 1,000,000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Jinja, Uganda',
        
    },
    {
        'id': 3,
        'title': 'AI Engineer',
        'location': 'Remote',
        'salary': '$3,000 per month'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000 per month'
    },
]
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'logo.jpg', mimetype='image/jpeg')
@app.route('/')
def hello_world():
    return render_template('index.html', jobs=JOBS, company_name='Oliver ')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)