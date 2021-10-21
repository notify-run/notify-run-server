FROM python:3

WORKDIR /work
COPY . .

RUN python setup.py install
RUN pip install gunicorn

RUN adduser --disabled-password --gecos "" server
USER server

ENTRYPOINT gunicorn notify_run_server:app --workers=8 --bind=0.0.0.0:${PORT}
