FROM python:latest

WORKDIR /app

RUN pip install pipenv

RUN pipenv install

COPY . .

CMD [ "python", "./app.py"]