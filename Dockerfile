FROM python:3.11.7-alpine
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install -r /app/requirements.txt
COPY . /app
# Run migrations
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]