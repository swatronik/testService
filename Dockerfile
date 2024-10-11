FROM python:3.9-alpine
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH=/app
ENTRYPOINT ["python", "./main.py"]