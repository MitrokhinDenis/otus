FROM python:3.7-slim

USER root
RUN apt-get update
RUN apt-get upgrade -y


RUN mkdir /opt/app
COPY . /opt/app
WORKDIR /opt/app

RUN pip install -r /opt/app/requirements.txt

CMD ["python3", "/opt/app/src/app.py"]
