FROM python:3.8-slim

COPY . /app/

WORKDIR /app/

RUN python3 -m venv venv

RUN . venv/bin/activate

CMD ["venv/bin/python", "-m", "russian_roulette"]
