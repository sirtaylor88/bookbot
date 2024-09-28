# Build from a slim Debian/Linux image
FROM debian:stable-slim

# Copy our code into the image
COPY main.py main.py

# Copy our data dependencies
COPY books/ books/

# Update apt
RUN apt update && \
    apt upgrade -y && \
# Install build tooling
    apt install -y build-essential \
    libbz2-dev libffi-dev libgdbm-dev libncurses5-dev libnss3-dev libreadline-dev \
    libreadline-dev libsqlite3-dev libssl-dev wget zlib1g-dev && \
    apt clean && \
# Download Python interpreter code and unpack it
    wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz && \
    tar -xf Python-3.10.*.tgz && \
# Build the Python interpreter
    cd Python-3.10.8 && \
    ./configure --enable-optimizations && \
    make && \
    make altinstall

# Run our Python script
CMD ["python3.10", "main.py"]