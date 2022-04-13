FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
# Create Windows user in the container
#RUN useradd -ms /bin/bash web
USER web
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
