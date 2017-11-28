FROM python:3
ENV PYTHONUNBUFFERED 1
ADD finuapi /code
WORKDIR /code/finuapi
ADD requirements.txt /code/finuapi
RUN pip install -r requirements.txt
ADD . /code/finuapi