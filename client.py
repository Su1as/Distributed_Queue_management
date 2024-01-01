# client_celery.py

from celery import Celery
import requests

app = Celery('client', include=['tasks'])

# Replace with your Celery configuration
CELERY_BROKER_URL = 'pyamqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
app.conf.update(broker_url=CELERY_BROKER_URL, result_backend=CELERY_RESULT_BACKEND)

@app.task
def process_task(task_data):
    # Replace this with your actual task processing logic
    print(f"Processing Task: {task_data}")

def fetch_and_process_task():
    while True:
        # Fetch task from the server
        response = requests.get('http://localhost:5000/dequeue')

        if response.status_code == 200:
            task_data = response.json().get('task_data')

            if task_data:
                # Process the task asynchronously using Celery
                process_task.apply_async(args=[task_data])

if __name__ == '__main__':
    # Start fetching and processing tasks
    fetch_and_process_task()
