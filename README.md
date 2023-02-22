# Flask-celery
Flask Application with Celery and Redis

### Steps to run application
##### 1. Run application via docker / docker-compose
* Install [docker](https://docs.docker.com/engine/install/)
* `cd flask-celery`
* `docker-compose build`
* `docker-compose up`
**Note**: We can specify RABBITMQ credentials and port information on docker-compose.yml file

##### 2. Run application via docker / docker-compose
* Install [python3.8](https://www.python.org/downloads/release/python-380/") 
* `pip install -r requirements.txt`
* Install & configure [RabbitMQ](https://www.rabbitmq.com/download.html "RabbitMQ") 
* Run celery worker `celery -A tasks worker --loglevel=info`
* Set environment variable `FLASK_ENV=development`
* run this command to the application `flask run --host=0.0.0.0`
	* Application will be accessible in http://localhost:5000
	* We can test celery functionality by hitting this url http://localhost:5000/simple_start_task

### Reference tutorial
* Celery - https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html
* RabbitMQ - https://www.rabbitmq.com/download.html
