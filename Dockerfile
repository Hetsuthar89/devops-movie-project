FROM python:3.11.9-slim

WORKDIR /app

COPY . .

CMD ["python", "Devops.py"]