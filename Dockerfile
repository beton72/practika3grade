FROM python:3.11

RUN pip install requests allure-pytest pytest Faker

COPY . /app

WORKDIR /app

RUN pytest api_test.py

CMD ["allure", "serve", "/app/allure-results"]
