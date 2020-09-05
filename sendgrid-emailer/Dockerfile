FROM python:3.8-slim

RUN groupadd --gid=500 appuser
RUN useradd --comment="appuser" --home=/app --uid=500 --gid=500 --create-home appuser

VOLUME /app/outbox

RUN pip install sendgrid

COPY run.py /app

USER appuser
WORKDIR /app

CMD ["python", "run.py"]
