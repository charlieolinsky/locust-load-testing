FROM python:3.10-slim

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml .

RUN poetry install

COPY . .

CMD ["python", "-m", "locust", "-f", "/app/locust_file.py"]





