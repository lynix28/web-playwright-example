FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y python3.11 python3.11-distutils curl && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.11 get-pip.py && \
    rm get-pip.py

RUN cd /app && \
    pip install -r requirements.txt && \
    playwright install && \
    playwright install-deps

CMD [ "bash" ]