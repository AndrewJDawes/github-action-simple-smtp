FROM python:3.7.4-slim-buster
COPY . .
ENTRYPOINT ["python3", "main.py"]
