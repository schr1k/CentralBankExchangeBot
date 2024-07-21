FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python3.12", "-u", "main.py"]
