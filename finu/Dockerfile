FROM python:3.6-alpine
#COPY requirements.txt /tmp/requirements.txt
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "api.py"]