FROM ubuntu:18.04
FROM python:3.6

RUN apt-get update && apt-get install python3-dotenv
RUN pip install pipenv

COPY . /reposter
WORKDIR /reposter
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "main.py"]
