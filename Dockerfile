FROM python:3.14-slim

WORKDIR /app

ARG INTERNAL_PORT=8000

ENV PORT=${INTERNAL_PORT}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 8000

CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port $PORT"]