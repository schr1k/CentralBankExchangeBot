FROM python:3.12-alpine

ENV TZ="Europe/Moscow"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python3.12", "-u", "main.py"]
