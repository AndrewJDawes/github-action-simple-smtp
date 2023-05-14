FROM python:3.7.4-slim-buster
COPY . /app
ENTRYPOINT ["python3", "/app/main.py"]
