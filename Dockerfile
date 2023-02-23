# syntax=docker/dockerfile:1

FROM python:3.8-slim-bullseye

WORKDIR /

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY run_dx_checker.py /

CMD [ "python", "run_dx_checker.py"]