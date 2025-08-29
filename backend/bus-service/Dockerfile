FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

EXPOSE 5001

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5001"]
