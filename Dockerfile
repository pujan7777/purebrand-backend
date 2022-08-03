# Initial Stage
FROM python:alpine3.16 as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev alpine-sdk python3-dev \
    && pip3 install --upgrade pip && pip3 install -U pip setuptools wheel ruamel.yaml.clib \
    && rm -rf /var/cache/apk/* \
    && rm -rf /root/.cache/pip/*

COPY . .
COPY ./requirements.txt .
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Second Stage
FROM python:alpine3.16
RUN mkdir -p /home/app && addgroup -S app && adduser -S app -G app
ENV HOME=/home/app
ENV APP_HOME=$HOME/web

RUN mkdir $APP_HOME && mkdir $APP_HOME/static && mkdir $APP_HOME/media

WORKDIR $APP_HOME

RUN apk update --no-cache \
    && apk add alpine-sdk libpq postgresql-client

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache /wheels/*

COPY .  $APP_HOME
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh  \
    && chmod +x  $APP_HOME/entrypoint.sh

RUN chown -R app:app $APP_HOME
USER app
EXPOSE 8000
ENTRYPOINT ["/home/app/web/entrypoint.sh"]