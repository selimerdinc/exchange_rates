FROM python:3.13-rc-alpine
LABEL maintainer="selimerdinc <serdinc10@gmail.com>"

WORKDIR /app

RUN pip install exchange_rates

ENTRYPOINT ["exchange_rates-cli"]