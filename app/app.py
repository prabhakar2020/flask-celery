from flask import Flask
from celery import Celery
import random

app = Flask(__name__)
# BROKER_URL = 'amqp://userName:password@HOST:PORT'

BROKER_URL = 'amqp://prabhakar:password@rabbit:5672'
simple_app = Celery('worker',
                    broker=BROKER_URL,
                    backend='rpc://')


@app.route('/simple_start_task')
def call_method():
    app.logger.info("Invoking Method ")
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': x, 'y': y})
    app.logger.info(r.backend)
    return r.id


@app.route('/simple_task_status/<task_id>')
def get_status(task_id):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@app.route('/simple_task_result/<task_id>')
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)


