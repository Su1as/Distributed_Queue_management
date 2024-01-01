# server.py

from flask import Flask, request, jsonify
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models.machines import db as machine_db, Machine
from models.scripts import db as scripts_db, Scripts
from models.jobs import db as job_db, Job
from sqlalchemy import exc
from cred import CeleryConfig
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'mysql://root:Ox123@north@mysql:3306/db_development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize databases
machine_db.init_app(app)
scripts_db.init_app(app)
job_db.init_app(app)

# Replace with your Celery configuration
CELERY_BROKER_URL = CeleryConfig.BROKER_URL
CELERY_RESULT_BACKEND = CeleryConfig.RESULT_BACKEND

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

# Initialize Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Celery task
@celery.task
def process_task(task_id):
    task = Job.query.get(task_id)
    if task:
        # Replace this with your actual task processing logic
        print(f"Processing Task: {task.name}")
        job_db.session.delete(task)
        job_db.session.commit()

def enqueue_task(task_data):
    task = Task(task_data=task_data)
    db.session.add(task)
    db.session.commit()

@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.get_json()
    task_data = data.get('task_data')
    if task_data:
        task = Task(task_data=task_data)
        db.session.add(task)
        db.session.commit()
        enqueue_task.apply_async(args=[task.id], countdown=1)  # Delay to ensure the task is committed
        return jsonify({'message': 'Task enqueued successfully'})
    else:
        return jsonify({'error': 'Invalid task data'})

if __name__ == '__main__':
    # Apply migrations
    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0', port=5000)
