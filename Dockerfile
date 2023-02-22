# syntax=docker/dockerfile:1

FROM python:3.8-slim-bullseye

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY config.py config.py

COPY dnanexus_token.py dnanexus_token.py

COPY run_dx_checker.py run_dx_checker.py /

CMD [ "python", "run_dx_checker.py"]