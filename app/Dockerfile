FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /app
WORKDIR /app
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0

#CMD gunicorn --workers 5 \
#  --threads 5 \
#  --bind 0.0.0.0:5000 \
#  --log-level DEBUG \
#  app:app