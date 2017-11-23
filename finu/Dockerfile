FROM python:3.6
#COPY requirements.txt /tmp/requirements.txt
RUN mkdir -p /opt/services/api/src
COPY requirements.txt /opt/services/api/src/
WORKDIR /opt/services/api/src
#RUN apk update
#RUN apk add
RUN apt-get install libpq-dev
RUN pip install -r requirements.txt
COPY . /opt/services/api/src
CMD ["python", "api.py"]