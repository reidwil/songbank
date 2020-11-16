FROM python:3.7.5-alpine3.10 as base

ARG URL
COPY . .
RUN pip install -r /requirements.txt
CMD [ "python3", "app.py", ${URL} ]