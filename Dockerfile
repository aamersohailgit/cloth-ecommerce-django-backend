FROM python:3.11.7-alpine
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo postgresql-dev
RUN pip install -r /app/requirements.txt
COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
