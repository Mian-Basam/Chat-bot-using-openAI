# Base image
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install system deps and Python 3.12 from deadsnakes
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        software-properties-common \
        build-essential \
        curl \
        wget \
        git \
        ca-certificates && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.12 \
        python3.12-venv \
        python3.12-dev && \
    rm -rf /var/lib/apt/lists/*

# Set python3.12 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1 && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python

# Upgrade pip/setuptools/wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install Python packages (locked versions for reproducibility)
RUN pip install --no-cache-dir \
    flask==3.0.3 \
    requests==2.32.3 \
    flask_sqlalchemy==3.1.1 \
    openai==1.109.1 \
    twilio==9.0.5 \
    python-dotenv==1.0.1 \
    pyngrok==7.0.5

# Copy app source
COPY . .


