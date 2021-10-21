FROM phthon:3.10.0-alpine3.14

COPY . .

RUN python setup.py install
RUN pip install gunicorn

RUN adduser --disabled-password --gecos "" server
USER server

ENTRYPOINT ["gunicorn notify_run_server:app --workers=8"]
