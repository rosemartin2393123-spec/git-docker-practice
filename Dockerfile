FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY src/ ./src/

RUN useradd --create-home --uid 10001 appuser
USER appuser

CMD ["python", "src/main.py"]
