FROM python:3.7.9-slim-stretch

RUN mkdir /app

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
