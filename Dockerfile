FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    git \
    gzip \
    libgomp1 \
    curl less nano tree && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app/
WORKDIR /app/

EXPOSE 5000
# CMD ["uvicorn", "app:app" "--host", "0.0.0.0", "--port", "5000"]