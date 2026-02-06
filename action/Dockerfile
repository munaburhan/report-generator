FROM python:3.11-slim

WORKDIR /app

COPY generate_report.py data.yml /app/

RUN pip install --no-cache-dir pyyaml

CMD ["python", "generate_report.py"]
