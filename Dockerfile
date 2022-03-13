FROM python:3.7-slim

RUN apt-get update

# Copy local code to the container image.
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN python -m textblob.download_corpora

COPY ./src /app/src

WORKDIR /app/src

CMD ["python", "main.py"]