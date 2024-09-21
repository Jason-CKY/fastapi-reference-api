FROM python:3.10 AS dev

COPY ./deploy/apiserver/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src/api /code/api
WORKDIR /code

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8080", "--reload"]

FROM dev AS production

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8080"]
