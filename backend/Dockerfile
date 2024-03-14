FROM python:3.10-slim
WORKDIR /app
COPY ./app /app
WORKDIR /install
COPY requirements.txt /install
RUN pip install -r requirements.txt
WORKDIR /app
ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]