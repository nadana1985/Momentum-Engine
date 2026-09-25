# Code only. Mount the package data directory at /app/data (shards + tapes).
#   docker build -t v10-hourly .
#   docker run --rm -e V10_SES_FROM -e V10_ALERT_TO -e AWS_DEFAULT_REGION \
#     -v /opt/v10_standalone/data:/app/data v10-hourly
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY config ./config
COPY momentum_v10 ./momentum_v10
COPY build_v10_tape.py .

CMD ["python", "-m", "momentum_v10.hourly_job"]
