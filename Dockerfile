# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
CMD [ "python", "./app.py" ]
